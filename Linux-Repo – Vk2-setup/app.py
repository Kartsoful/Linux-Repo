# Toimiva app.py tiedosto
# Palauttaa SQL-palvelimen ajan ja tallentaa Speden pelin pisteet MySQL-tietokantaan

from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# --- tietokantayhteys ---
def db():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="user",          # vaihda omiin
        password="password",   # vaihda omiin
        database="database"    # vaihda omiin
    )

# --- etusivu ---
@app.route("/")
def home():
    conn = db()
    cur = conn.cursor()
    cur.execute("SELECT NOW()")
    ts = cur.fetchone()[0]
    cur.close(); conn.close()
    return f"<h1>Hello from MySQL!</h1><p>SQL-palvelimen aika: <b>{ts}</b></p>"

# --- kellonajan API ---
@app.route("/time")
def time_api():
    conn = db()
    cur = conn.cursor()
    cur.execute("SELECT NOW()")
    ts = cur.fetchone()[0]
    cur.close(); conn.close()
    return jsonify({"time": str(ts)})

# --- pisteiden tallennus ---
@app.route("/score", methods=["POST"])
def score_post():
    data = request.get_json(silent=True) or {}
    nickname = (data.get("nick") or "anon")[:32]
    try:
        score = int(data.get("score", 0))
    except (TypeError, ValueError):
        return jsonify({"ok": False, "error": "bad score"}), 400

    if score < 0 or score > 1_000_000:
        return jsonify({"ok": False, "error": "range"}), 400

    conn = db()
    cur = conn.cursor()
    cur.execute("INSERT INTO highscores (nickname, score) VALUES (%s, %s)", (nickname, score))
    conn.commit()
    cur.close(); conn.close()
    return jsonify({"ok": True})

# --- top-lista ---
@app.route("/scores", methods=["GET"])
def scores_get():
    conn = db()
    cur = conn.cursor()
    cur.execute("""
        SELECT nickname, score, created_at
        FROM highscores
        ORDER BY score DESC, created_at ASC
        LIMIT 10;
    """)
    rows = cur.fetchall()
    cur.close(); conn.close()
    return jsonify([{"nick": r[0], "score": int(r[1]), "at": str(r[2])} for r in rows])

# --- sovellus käyntiin ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
