from app import app

from flask import render_template

@app.route("/")
def hello_world():


    
    headers = {"TRN-Api-Key": "c8288c3c-1d53-407a-926c-0e851d083a02"}
    return render_template("public/index.html")