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
        password="pass",   # vaihda omiin
        database="db"    # vaihda omiin
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



