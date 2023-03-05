from flask import jsonify, render_template, request, session

from app import app
from app.db.db_config import db
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
    BF_games = db.execute("SELECT * FROM BF_games") 
    modes = db.execute("SELECT * FROM modes")
    highScores = []


    for BF_game in BF_games:
        scores = {
            "BF_game": BF_game["short_name"],
            "modes":{}
        }
        for mode in modes:
            score = db.execute("""SELECT MAX(score) AS highest_score 
                FROM game_log 
                WHERE user_id = ? AND BF_game = ? AND mode = ?"""
                , session["user_id"], BF_game["short_name"], mode["mode"])  
            difficulty = mode["mode"]
            scores["modes"][difficulty] = score[0]["highest_score"]

        highScores.append(scores)  
        # highScore data structure:
        # {
        #     "BF_game": "BF_game (eg BF4)",
        #     "mode": {
        #         "easy": highest_score,
        #         "medium": highest_score,
        #         "hard": highest_score
        #         }
            
        # }

    return jsonify(highScores=highScores, modes=modes)

@app.route("/edit-account", methods=["GET", "POST"])
@login_required
def edit_details():

    if request.method == "POST":
        rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        current_email_address = rows[0]["email_address"]
        current_username = rows[0]["username"]

        new_email_address = request.form.get("email-address")
        new_username = request.form.get("username")

        db.execute("""        
        UPDATE users
        SET username = ?, email_address = ?
        WHERE id = ?
        """, new_username, new_email_address, session["user_id"])

        return render_template("public/index.html")
    else:
        # Get user's email and username on db
        # Populate those details on input box in edit-account.html
        rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        email_address = rows[0]["email_address"]
        if not email_address:
            email_address = ""
        
        username = rows[0]["username"]

        return render_template("admin/edit-account.html", email_address=email_address, username=username)
    

@app.route("/edit-account/email_address")
@login_required
def find_current_email_address():
    rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    current_email_address = rows[0]["email_address"]
    current_username = rows[0]["username"]

    new_email_address = request.form.get("email-address")
    new_username = request.form.get("username")

    email_address = request.args.get("email-address")
    username = request.args.get("username")

    if email_address:
        rows = db.execute("SELECT email_address FROM users WHERE email_address = ?", new_email_address)
        # if row is empty or rows["email_address"] == current_email_address:
            # continue
        # else
            # disable edit account

        if len(rows) == 1 and rows[0]["email_address"] != current_email_address:
            return jsonify(rows[0]["email_address"])
    
    if username:
        rows = db.execute("SELECT username FROM users WHERE username = ?", new_username)
        # if row is empty or rows["username"] == current_username:
            # continue
        # else
            # disable edit account



@app.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():

    if request.method == "POST":
        return render_template("public/index.html")
    else:
        return render_template("admin/change-password.html")