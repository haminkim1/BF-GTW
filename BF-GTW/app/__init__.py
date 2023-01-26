from flask import Flask
from app.db.init_db import init_db
from flask_session import Session

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

init_db()

from app import auth, home, games