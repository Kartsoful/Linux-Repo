# Toimiva app.py tiedosto
# Tiedostossa tietokantayhteys joka palauttaa kellonajan
# Muokkaa db-funktioon host, user, password sekä database vastaamaan MySQL-tietoja

from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def db():
    return mysql.connector.connect(
        host="localhost,
        user="user",
        password="salasana",
        database="tietokannan nimi"
    )

@app.route("/")
def home():
    conn = db(); cur = conn.cursor()
    cur.execute("SELECT NOW()")
    ts = cur.fetchone()[0]
    cur.close(); conn.close()
    return f"<h1>Hello from MySQL!</h1><p>SQL-palvelimen aika: <b>{ts}</b></p>"

@app.route("/time")
def time_api():
    conn = db(); cur = conn.cursor()
    cur.execute("SELECT NOW()")
    ts = cur.fetchone()[0]
    cur.close(); conn.close()
    return jsonify({"time": str(ts)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
