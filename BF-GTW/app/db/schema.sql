DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    email_address varchar(32) UNIQUE, --NOT NULL
    username varchar(20) NOT NULL UNIQUE,
    hash TEXT NOT NULL
)

