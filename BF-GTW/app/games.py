from app import app
from modules.auth_modules import *
from modules.image_map_scraping import scrapeImages

from flask import render_template

@app.route("/games")
def display_games():

    images = scrapeImages()
    return render_template("public/games.html", images=images)