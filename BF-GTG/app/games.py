from app import app
from modules.auth_modules import test

from flask import render_template

@app.route("/games")
def display_games():
    hello = test()
    print(hello)
    return render_template("public/games.html")