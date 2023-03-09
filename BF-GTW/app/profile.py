from flask import jsonify, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash

from app import app
from app.db.db_config import db
from modules.auth_modules import change_user_password, delete_user, login_required
from modules.games_modules import delete_game_logs


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
            "modes":{},
            "date": {}
        }
        for mode in modes:
            score = db.execute("""SELECT MAX(score) AS highest_score, DATE(game_date) AS game_date
                FROM game_log 
                WHERE user_id = ? AND BF_game = ? AND mode = ?"""
                , session["user_id"], BF_game["short_name"], mode["mode"])  
            difficulty = mode["mode"]
            scores["modes"][difficulty] = score[0]["highest_score"]
            scores["date"][difficulty] = score[0]["game_date"]

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
    

@app.route("/edit-account/check_email_exist")
@login_required
def check_email_address_exist():
    current_email_address = session["email_address"]
    email_address = request.args.get("email_address")

    if email_address:
        rows = db.execute("SELECT email_address FROM users WHERE email_address = ?", email_address)
        if not rows or current_email_address == email_address:
            email_exists = False
        else:
            email_exists = True
        return jsonify(emailExists=email_exists)
    

@app.route("/edit-account/check_username_exist")
@login_required
def check_username_exist():
    current_username = session["username"]
    username = request.args.get("username")

    if username:
        rows = db.execute("SELECT username FROM users WHERE username = ?", username)
        if not rows or current_username == username:
            username_exists = False
        else:
            username_exists = True
        return jsonify(usernameExists=username_exists)


@app.route("/change-password", methods=["POST"])
@login_required
def change_password():
    password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
    change_user_password(session["user_id"], password)
    return render_template("admin/change-password.html")
    

@app.route("/delete-account", methods=["POST"])
@login_required
def delete_account():

    delete_game_logs(session["user_id"])
    delete_user(session["user_id"])
    session.clear()

    return redirect("/")