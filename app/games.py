from flask import render_template, request

from app import app
from modules.auth_modules import *
from modules.games_modules import check_game_over, display_game_over_data
from modules.image_map_scraping import scrapeImages

@app.route("/games")
@login_required
def display_games():

    images = scrapeImages()
    return render_template("public/games/games.html", images=images)

# Game over/winner feature
# Redirect user to game_over.html if they either win or lose the game
# The page should have:
#     Message statement for winner/loser
#     Show what mode was played
#         Might need to create a session["mode"] if it's easier to code with it
#     Show which BF game was played 
#         Might need to create a session["BF_game"] or a similar name
#     Show score over total weapon for either win/lose case. 
#         User session["current_score"] and session["total_weapons"]
#     Play again button
#         redirect to games.html
#     Quit button
#         redirect to index.html
@app.route("/game_over")
@login_required
# As /game_over is a get request, @check_game_over prevents user from visiting game_over.html
# without playing any games. 
@check_game_over
def game_over():
    session["game_over"] = False
    # Create data dictionary and pass along relevant session. 
    # render data to game_over.html
    data = display_game_over_data()
    
    return render_template("public/games/game_over.html", data=data)