from app import app

from flask import render_template

@app.route("/register")
def register():
    return render_template("admin/register.html")

@app.route("/login")
def login():
    return render_template("admin/login.html")