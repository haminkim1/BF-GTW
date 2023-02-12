from flask import render_template, request

from app import app
from modules.auth_modules import *
from modules.image_map_scraping import scrapeImages

@app.route("/games")
@login_required
def display_games():

    images = scrapeImages()
    return render_template("public/games/games.html", images=images)


@app.route("/game_over")
# Put a wrapper to prevent user from accessing /game_over directly from the URL
# If user directly types /game_over on the URL, redirect to home like how
# @login_required does
@login_required
def game_over():
    return render_template("public/games/game_over.html")