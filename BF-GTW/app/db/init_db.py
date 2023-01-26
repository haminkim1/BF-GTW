from .db_config import db

def init_db():
    with open('app/db/schema.sql', 'r') as f:
        sql = f.read()
        statements = sql.split(';')
        for statement in statements:
            db.execute(statement)