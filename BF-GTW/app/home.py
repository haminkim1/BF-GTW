from flask import render_template

from app import app
from modules.apology import apology

@app.route("/")
def home():
    return render_template("public/index.html")

@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>', methods=['GET'])
def catch_all(path):
    return apology("Route does not exist")