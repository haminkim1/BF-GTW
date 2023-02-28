from flask import render_template, session

from app import app
from app.db.db_config import db
from modules.apology import apology

@app.route("/")
def home():
    if session:
        rows = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])
        username = rows[0]["username"]
        return render_template("public/index.html", username=username)
    else:
        return render_template("public/index.html")

@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>', methods=['GET'])
def catch_all(path):
    return apology("Route does not exist")