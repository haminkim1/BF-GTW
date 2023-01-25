from app import app
from flask import render_template

from modules.apology import apology

@app.route("/")
def hello_world():
    return render_template("public/index.html")

@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>', methods=['GET'])
def catch_all(path):
    return apology("Route does not exist")