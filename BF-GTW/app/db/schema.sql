CREATE TABLE IF NOT EXISTS users (
    id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    email_address varchar(32) UNIQUE, --NOT NULL
    username varchar(20) NOT NULL UNIQUE,
    hash TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS play_without_account_users (
    id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    username varchar(20) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS bfv_weapons (
    weapon_id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    weapon_name text NOT NULL,
    weapon_type text NOT NULL,
    weapon_image text NOT NULL -- /static/images/bfvImages/easy/1.png
)