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

    # Selects logged in user's highest score from easy, medium, hard mode for BF4, BF1, BFV, BF2042
    # Insert score/total_weapons on top, DATE(game_date) on bottom as a split cell. 
    """
            easy|medium|high
    BF4     S/T_W
            date
    BF1     S/T_W
            date
    BFV     S/T_W
            date
    BF2042  S/T_W
            date
    """
    
    bf4HighScores = db.execute("""SELECT UPPER(BF_game), mode, MAX(score) AS highest_score, total_weapons, DATE(game_date) 
    FROM game_log 
    WHERE user_id = ? AND BF_game IN ('bf4') AND mode IN ('easy', 'medium', 'hard') 
    GROUP BY BF_game, mode 
    ORDER BY 
        CASE 
            WHEN mode = 'easy' THEN 1 
            WHEN mode = 'medium' THEN 2 
            WHEN mode = 'hard' THEN 3 
        END""", session["user_id"])
    
    bf1HighScores = db.execute("""SELECT UPPER(BF_game), mode, MAX(score) AS highest_score, total_weapons, DATE(game_date) 
    FROM game_log 
    WHERE user_id = ? AND BF_game IN ('bf1') AND mode IN ('easy', 'medium', 'hard') 
    GROUP BY BF_game, mode 
    ORDER BY 
        CASE 
            WHEN mode = 'easy' THEN 1 
            WHEN mode = 'medium' THEN 2 
            WHEN mode = 'hard' THEN 3 
        END""", session["user_id"])
    
    bfvHighScores = db.execute("""SELECT UPPER(BF_game), mode, MAX(score) AS highest_score, total_weapons, DATE(game_date) 
    FROM game_log 
    WHERE user_id = ? AND BF_game IN ('bfv') AND mode IN ('easy', 'medium', 'hard') 
    GROUP BY BF_game, mode 
    ORDER BY 
        CASE 
            WHEN mode = 'easy' THEN 1 
            WHEN mode = 'medium' THEN 2 
            WHEN mode = 'hard' THEN 3 
        END""", session["user_id"])

    bf2042HighScores = db.execute("""SELECT UPPER(BF_game), mode, MAX(score) AS highest_score, total_weapons, DATE(game_date) 
    FROM game_log 
    WHERE user_id = ? AND BF_game IN ('bf2042') AND mode IN ('easy', 'medium', 'hard') 
    GROUP BY BF_game, mode 
    ORDER BY 
        CASE 
            WHEN mode = 'easy' THEN 1 
            WHEN mode = 'medium' THEN 2 
            WHEN mode = 'hard' THEN 3 
        END""", session["user_id"])
    
    # highScores = db.execute("""SELECT UPPER(BF_game), mode, MAX(score) AS highest_score, total_weapons, DATE(game_date) 
    # FROM game_log 
    # WHERE user_id = ? AND BF_game IN ('bf4', 'bf1', 'bfv', 'bf2042') AND mode IN ('easy', 'medium', 'hard') 
    # GROUP BY BF_game, mode 
    # ORDER BY 
    #     CASE 
    #         WHEN BF_game = 'bf4' THEN 1 
    #         WHEN BF_game = 'bf1' THEN 2 
    #         WHEN BF_game = 'bfv' THEN 3 
    #         WHEN BF_game = 'bf2042' THEN 4 
    #     END, 
    #     CASE 
    #         WHEN mode = 'easy' THEN 1 
    #         WHEN mode = 'medium' THEN 2 
    #         WHEN mode = 'hard' THEN 3 
    #     END""", session["user_id"])
    
    # print(highScores)
    print(bfvHighScores)

    # get list of BF_games from table
    # get list of modes from table
    # Use a loop for each combination of BF_games and modes
    # Create empty highScores list
    # Starting at BF4, BF1, BFV, BF2042:
        # if BF_games & modes have score, leave as is
        # else somehow put an empty data 
        # Append to highScores list
        # Repeat for other combinations
    # Send highScores list to client
    highScores = []
    BF_games = ["bf4", "bf1", "bfv", "bf2042"]
    modes = ["easy", "medium", "hard"]

    
    for BF_game in BF_games:
        for mode in modes:
            score = db.execute("""SELECT MAX(score) AS highest_score FROM game_log WHERE user_id = ? AND BF_game = ? AND mode = ?"""
                   , session["user_id"], BF_game, mode)  
            print(score)
            if not score:
                score[0] = None
            highScores.append(score[0])
    print(highScores)
    


    return render_template("admin/profile.html", usersData=usersData, games=games)

@app.route("/profile/highscore")
@login_required
def load_highscore():
    BF_games = ["bf4", "bf1", "bfv", "bf2042"]
    modes = ["easy", "medium", "hard"]

    # To automate the process, each variable name can be such as one, two or three instead of bf4highscores. 
    # The BF_game value that'll be passed to client will be the HEADING for each row. 
    bf4HighScores = {
        "BF_game": "BF4",
        "mode":[
            {"easy": 1,
            "medium": 2,
            "hard": 3
            }
        ]
    }
    print(bf4HighScores["mode"][0]["easy"])
    bf1HighScores = {
        "BF_game": "BF1",
        "easy": 4,
        "medium": 5,
        "hard": 6
    }

    highScores = []

    for BF_game in BF_games:
        scores = {
            "BF_game": BF_game,
            "modes":modes
        }

        for index, mode in enumerate(modes):
            score = db.execute("""SELECT MAX(score) AS highest_score FROM game_log WHERE user_id = ? AND BF_game = ? AND mode = ?"""
                   , session["user_id"], BF_game, mode)  
            scores["modes"][index][mode] = score[0]["highest_score"]

        highScores.append(scores)
    

    return jsonify(highScores)