from flask import render_template

from app import app
from modules.apology import apology
from modules.auth_modules import login_required

@app.route("/bf2042")
@login_required
def bf2042_route():
    return render_template("public/games/bf2042.html")

