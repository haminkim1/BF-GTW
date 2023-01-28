from flask import render_template, redirect, request, session, jsonify, make_response
import nltk
from nltk.corpus import wordnet
from werkzeug.security import check_password_hash, generate_password_hash

from datetime import datetime, timedelta
import random as rand

from app import app
from app.db.db_config import db
from modules.apology import apology
from modules.auth_modules import login_required
from modules.image_map_scraping import scrapeImages

# DON'T DELETE THIS FOR NOW, related to no_account_login route
nltk.download('wordnet')

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # If user didn't enter any username, return apology
        if not request.form.get("username"):
            return apology("Enter username", 403)

        # Check if user's input for username already exists. If exist, return apology
        elif db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username")):
            return apology("Username already exists", 403)

        else:
            username = request.form.get("username")
            password = request.form.get("password")
            confirmation = request.form.get("confirmation")

            # If password and repeat password doesn't match, return apology allow user to re-type password again.
            if not password or password != confirmation:
                return apology("Password must not be empty and match with repeat password", 403)

            # If all the checks pass, register username and hash password into users table. Redirect to home page logged in.
            else:
                password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
                db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, password)

                rows = db.execute("SELECT * FROM users WHERE username = ?", username)
                session["user_id"] = rows[0]["id"]

                # Redirect user to home page
                username = request.form.get("username")
                toastMessage = "Welcome, {}".format(username)
                response = make_response(redirect("/"))
                response.set_cookie('toastMessage', toastMessage, max_age=1)
                return response

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("admin/register.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)
        
        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Sending toastmessage to homepage indicating user they have successfully logged in. 
        username = request.form.get("username")
        toastMessage = "Welcome, {}".format(username)
        response = make_response(redirect("/"))
        response.set_cookie('toastMessage', toastMessage, max_age=1)
        # Redirect user to home page
        return response
        
    else:
        return render_template("admin/login.html")


@app.route("/no_account_login", methods=["POST"])
def no_account_login():

    # try:
        adj_synsets = wordnet.all_synsets(pos='a')
        adj_lemmas = [lemma.name() for synset in adj_synsets for lemma in synset.lemmas()]
        noun_synsets = wordnet.all_synsets(pos='n')
        noun_lemmas = [lemma.name() for synset in noun_synsets for lemma in synset.lemmas()]
        username = rand.choice(adj_lemmas) + rand.choice(noun_lemmas)
        print (f"username is {username}")
        db.execute("INSERT INTO play_without_account_users (username) VALUES(?)", username)

        rows = db.execute("SELECT * FROM play_without_account_users WHERE username = ?", username)
        session["user_id"] = rows[0]["id"]
    # except:
        # # Sending toastmessage to homepage indicating user they have successfully logged in. 
        # toastMessage = "Failed to play without creating logging in, please try again"
        # response = make_response(redirect("/"))
        # response.set_cookie('toastMessage', toastMessage, max_age=1)
        # # Redirect user to home page
        # return response


        
        # Instead of importing from modules.image_map_scraping import scrapeImages and 
        # typing the below code, see if I can import display_games() function from games.py route. 
        images = scrapeImages()
        return render_template("public/games/games.html", images=images)


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    print(session)
    session.clear()

    # Redirect user to login form
    return redirect("/")