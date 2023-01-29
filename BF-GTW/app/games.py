from flask import render_template

from app import app
from modules.auth_modules import *
from modules.image_map_scraping import scrapeImages

@app.route("/games")
@login_required
def display_games():

    images = scrapeImages()
    return render_template("public/games/games.html", images=images)