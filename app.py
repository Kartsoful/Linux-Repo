# Toimiva app.py tiedosto
# Palauttaa SQL-palvelimen ajan ja tallentaa Speden pelin pisteet MySQL-tietokantaan

from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# --- tietokantayhteys ---
def db():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="kartso",          # vaihda omiin
        password="kartso123",   # vaihda omiin
        database="exampledb"    # vaihda omiin
    )

# --- kellonajan API ---
@app.route("/time")
def time_api():
    conn = db()
    cur = conn.cursor()
    cur.execute("SELECT NOW()")
    ts = cur.fetchone()[0]
    cur.close(); conn.close()
    return jsonify({"time": str(ts)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


