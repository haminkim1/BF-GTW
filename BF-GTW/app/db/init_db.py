import json
import random
import requests

from .db_config import db

def init_db():
    with open('app/db/schema.sql', 'r') as f:
        sql = f.read()
        statements = sql.split(';')
        for statement in statements:
            db.execute(statement)
    init_bfv_weapons_db()


def init_bfv_weapons_db():
    # Getting API data. 
    response_API = requests.get('https://api.gametools.network/bfv/weapons/?format_values=true&name=HAMINATOR1997&platform=pc&skip_battlelog=false&lang=en-us')
    data = response_API.text
    # Converting API data into JSON. 
    jsonData = json.loads(data)

    # Assigning only weapons data into weapon variable
    weapons = jsonData["weapons"]

    rows = db.execute("SELECT COUNT(*) FROM bfv_weapons")
    # Get number of rows
    num_rows = rows[0]["COUNT(*)"]

    # If the number of weapons obtained from the API is larger than the number of rows in the table
    # (number of rows = number of weapons), delete the table and re-update. 
    # The len(weapons) can only be larger if new weapons were recently added to the API. 
    if num_rows < len(weapons):
        db.execute("DELETE FROM bfv_weapons")
        random.shuffle(weapons)
        for i in range(len(weapons)):
            db.execute("INSERT INTO bfv_weapons (weapon_name, weapon_type, weapon_image) VALUES(?, ?, ?)",
            weapons[i]["weaponName"], weapons[i]["type"], weapons[i]["image"])

    # Download images
    # Somehow get access to getImages.py under modules folder (or make a function here). 
    # Make a function on code lines 26 and below and pass in weapons[i]["image"] to the function. 
    # Use filename = url.split("/")[-1] to get the weapon name only instead of the entire url.
    # Save the image name using the password hash function against the filename. 
    # Would potentially need to make another column in the table called hashed_image
    # Would not be necessary to save the images in 3 folders (easy, med, hard), we can filter it out using the db instead.
    