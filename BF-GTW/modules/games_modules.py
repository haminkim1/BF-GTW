from flask import redirect, session
from functools import wraps

from app.db.db_config import db
from modules.apology import apology



def check_game_over(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("game_over") is False:
            return apology("Game is over")
        if session.get("game_over") is None:
            return redirect("/")
        return f(*args, **kwargs)
    return decorated_function


def data_for_next_round(i, round, previousWeaponName):
    data = {
    "weapon": session["weapons"][i]["encrypted_image_name"],
    "lives": session["lives"],
    "hints": session["hints"],
    "current_weapon": session["current_weapon"],
    "current_score": session["current_score"],
    "total_weapons": session["total_weapons"],
    "round": round,
    "consecutive_wins": session["consecutive_wins"],
    "previousWeaponName": previousWeaponName
    }
    return data


def display_game_over_data():
    rows = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])
    username = rows[0]["username"]

    data = {
        "username": username,
        "current_score": session["current_score"],
        "total_weapons": session["total_weapons"],
        "mode": session["mode"],
        "BF_game": session["BF_game"]
    }
    return data


def game_over():
    session["game_over"] = True
    session["play_state"] = False
    return session


def initialize_games_data(weapons):
    data = {
    "weapon": weapons[0],
    "lives": 3,
    "hints": 3,
    "current_weapon": 0,
    "current_score": 0,
    "total_weapons": len(weapons)
    }
    return data


def reset_games_sessions(data, mode, BF_game):
    session["lives"] = data["lives"]
    session["hints"] = data["hints"]
    session["current_weapon"] = data["current_weapon"]
    session["current_score"] = data["current_score"]
    session["total_weapons"] = data["total_weapons"]
    session["consecutive_wins"] = 0
    session["mode"] = mode
    session["BF_game"] = BF_game
    return session


def return_hint_data():
    # Getting first letter of weapon name.
    index_no = session["current_weapon"]
    first_letter = session["weapons"][index_no]["weapon_name"][0]

    data = {
        "hints": session["hints"],
        "weapon_type": session["weapons"][index_no]["weapon_type"],
        "first_letter": first_letter
    }
    return data


def save_game_data():
    db.execute("INSERT INTO game_log (user_id, mode, BF_game, score, total_weapons) VALUES (?, ?, ?, ?, ?)", session["user_id"], session["mode"], session["BF_game"], session["current_score"], session["total_weapons"])
