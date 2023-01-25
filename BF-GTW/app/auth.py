from app import app
from flask import render_template, redirect, request, session
from werkzeug.security import check_password_hash, generate_password_hash

from modules.auth_modules import login_required
from modules.apology import apology

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("Enter username")

        # Check if user's input for username already exists. If exist, return apology
        # Make a table from the database. 
        # elif db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username")):
        #     return apology("Username already exists")

        else:
            username = request.form.get("username")
            password = request.form.get("password")
            confirmation = request.form.get("confirmation")

            # If password and repeat password doesn't match, return apology allow user to re-type password again.
            if not password or password != confirmation:
                return apology("Password must not be empty and match with repeat password")

            # If all the checks pass, register username and hash password into users table. Redirect to home page logged in.
            else:
                password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
                db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, password)

                # rows = db.execute("SELECT * FROM users WHERE username = ?", username)
                # session["user_id"] = rows[0]["id"]

                return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("admin/register.html")

@app.route("/login")
def login():
    return render_template("admin/login.html")