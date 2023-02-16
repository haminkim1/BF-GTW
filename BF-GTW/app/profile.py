from flask import jsonify, render_template, session

from app import app
from app.db.db_config import db
from modules.apology import apology
from modules.auth_modules import login_required


@app.route("/profile")
@login_required
def view_profile():
    # Selects logged in user's email and username from users table from database.db
    rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    usersData = rows[0]

    # Selects logged in user's completed games
    games = db.execute("SELECT * FROM game_log WHERE user_id = ? ORDER BY game_date DESC", session["user_id"])

    return render_template("admin/profile.html", usersData=usersData, games=games)

@app.route("/profile/highscore")
@login_required
def load_highscore():
    BF_games = ["bf4", "bf1", "bfv", "bf2042"]
    modes = ["easy", "medium", "hard"]
    highScores = []

    # highScore data structure = {
    #     "BF_game": "BF_game (eg BF4)",
    #     "mode": {
    #         "easy": highest_score,
    #         "medium": highest_score,
    #         "hard": highest_score
    #         }
        
    # }
    for BF_game in BF_games:
        scores = {
            "BF_game": BF_game,
            "modes":{}
        }
        for mode in modes:
            score = db.execute("""SELECT MAX(score) AS highest_score 
                FROM game_log 
                WHERE user_id = ? AND BF_game = ? AND mode = ?"""
                , session["user_id"], BF_game, mode)  
            
            scores["modes"][mode] = score[0]["highest_score"]

        highScores.append(scores)   

    return jsonify(highScores)