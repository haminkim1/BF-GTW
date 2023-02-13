from flask import render_template

from app import app
from app.db.db_config import db
from modules.apology import apology
from modules.auth_modules import login_required


@app.route("/profile")
@login_required
def view_profile():

    return render_template("admin/profile.html")

