from flask import render_template

from app import app
from modules.apology import apology
from modules.auth_modules import login_required

@app.route("/bf1")
@login_required
def bf1_route():

    return render_template("public/games/bf1.html")

