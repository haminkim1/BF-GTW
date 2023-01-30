from flask import render_template

from app import app
from modules.apology import apology
from modules.auth_modules import login_required

@app.route("/bfv")
@login_required
def bfv_route():


    return render_template("public/games/bfv.html")

