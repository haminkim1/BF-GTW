from flask import redirect, session
from functools import wraps

from app.db.db_config import db



def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def change_user_password(id, hash):
    db.execute("""
    UPDATE users
    SET hash = ?
    WHERE id = ?
    """, id, hash)
    


def delete_user(id):
    db.execute("""
    DELETE FROM users
    WHERE id = ?
        """, id)
