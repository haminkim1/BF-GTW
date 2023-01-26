import sqlite3

DATABASE = 'database.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    return db

def init_db():
    db = get_db()
    with app.open_resourec('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120))
#     username = db.Column(db.String(120))
#     hash = db.Column(db.String(120))

#     def __init__(self, email, username, hash):
#         self.email = email
#         self.username = username
#         self.hash = hash