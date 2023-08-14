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
    weapon_image text NOT NULL,
    encrypted_image_name text NOT NULL
);


CREATE TABLE IF NOT EXISTS game_log (
    game_id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    user_id integer NOT NULL,
    mode varchar(10),
    BF_game varchar(10),
    score integer,
    total_weapons integer,
    game_date DATETIME DEFAULT (DATETIME('now')),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE IF NOT EXISTS game_log_without_account (
    game_id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    user_id integer NOT NULL,
    mode varchar(10),
    BF_game varchar(10),
    score integer,
    total_weapons integer,
    game_date DATETIME DEFAULT (DATETIME('now')),
    FOREIGN KEY (user_id) REFERENCES play_without_account_users (id)
);

CREATE TABLE IF NOT EXISTS BF_games (
    BF_id integer NOT NULL PRIMARY KEY,
    full_name varchar(32),
    short_name varchar(10)
);

CREATE TABLE IF NOT EXISTS modes (
    mode_id integer NOT NULL PRIMARY KEY,
    mode varchar(32),
    first_letter_cap varchar(32)
);

INSERT INTO BF_games (BF_id, full_name, short_name) 
SELECT 1, "Battlefield 4", "bf4"
WHERE NOT EXISTS (SELECT 1 FROM BF_games WHERE BF_id = 1);

INSERT INTO BF_games (BF_id, full_name, short_name) 
SELECT 2, "Battlefield 1", "bf1"
WHERE NOT EXISTS (SELECT 1 FROM BF_games WHERE BF_id = 2);

INSERT INTO BF_games (BF_id, full_name, short_name) 
SELECT 3, "Battlefield V", "bfv"
WHERE NOT EXISTS (SELECT 1 FROM BF_games WHERE BF_id = 3);

INSERT INTO BF_games (BF_id, full_name, short_name) 
SELECT 4, "Battlefield 2042", "bf2042"
WHERE NOT EXISTS (SELECT 1 FROM BF_games WHERE BF_id = 4);

INSERT INTO modes (mode_id, mode, first_letter_cap) 
SELECT 1, "easy", "Easy"
WHERE NOT EXISTS (SELECT 1 FROM modes WHERE mode_id = 1);

INSERT INTO modes (mode_id, mode, first_letter_cap) 
SELECT 2, "medium", "Medium"
WHERE NOT EXISTS (SELECT 1 FROM modes WHERE mode_id = 2);

INSERT INTO modes (mode_id, mode, first_letter_cap) 
SELECT 3, "hard", "Hard"
WHERE NOT EXISTS (SELECT 1 FROM modes WHERE mode_id = 3)
