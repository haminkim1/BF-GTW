from flask import render_template, session

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
    highScores = db.execute("""SELECT UPPER(BF_game), mode, MAX(score) AS highest_score, total_weapons, DATE(game_date) 
    FROM game_log 
    WHERE user_id = ? AND BF_game IN ('bf4', 'bf1', 'bfv', 'bf2042') AND mode IN ('easy', 'medium', 'hard') 
    GROUP BY BF_game, mode 
    ORDER BY 
        CASE 
            WHEN BF_game = 'bf4' THEN 1 
            WHEN BF_game = 'bf1' THEN 2 
            WHEN BF_game = 'bfv' THEN 3 
            WHEN BF_game = 'bf2042' THEN 4 
        END, 
        CASE 
            WHEN mode = 'easy' THEN 1 
            WHEN mode = 'medium' THEN 2 
            WHEN mode = 'hard' THEN 3 
        END""", session["user_id"])
    
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
    
    print(highScores)
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
    BF_games = ["bf4", "bf1", "bfv", "bf2042"]
    modes = ["easy", "medium", "hard"]
    


    return render_template("admin/profile.html", usersData=usersData, games=games, highScores=highScores)

