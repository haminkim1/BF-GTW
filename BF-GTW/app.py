from app import app
from flask_session import Session

if __name__ == "__main__":
    app.run()

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)