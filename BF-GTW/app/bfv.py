from flask import jsonify, redirect, render_template, request, session

from app import app
from modules.apology import apology
from modules.auth_modules import login_required
from modules.get_weapon_data import get_easy_mode_weapons, get_first_easy_weapon, get_hard_mode_weapons, get_medium_mode_weapons

import random

@app.route("/bfv", methods=["GET", "POST"])
@login_required
def bfv_route():
    # Getting hard mode weapons is pretty much retrieving every single weapon in the db. 
    allWeapons = get_hard_mode_weapons()
    weapon = get_first_easy_weapon(allWeapons)

    if request.method == "GET":
        weapons = session.get("weapons", [])
        lives = session.get("lives", [])
        hints = session.get("hints", [])

        # Get query parameter of key called "name"
        name = request.args.get("name")

        # If value of name key exists, cycle through each weapon name. 
        # If the weapon names start with name, append only the weapon name (not the entire object) to weaponNames list. 
        # Return weaponNames as JSON data back as a response to the client. 
        if name:
            weaponNames = []
            for i in range(len(weapons)):
                # If name == first letters of each list, return names as JSON object alphabetically
                if weapons[i]['weapon_name'].casefold().startswith(name.casefold()):
                    weaponNames.append(weapons[i]['weapon_name'])
            
            # Sorting the list alphabetically
            weaponNames = sorted(weaponNames)
            return jsonify(weaponNames)
        else:
            weaponNames = []

        return render_template("public/games/bfv.html", weapons=weapons, lives=lives, hints=hints, weapon=weapon)

    else:       
        mode = request.form.get("mode")
        if mode == "easy":
            weapons = get_easy_mode_weapons(allWeapons)
        elif mode == "medium":
            weapons = get_medium_mode_weapons(allWeapons)
        elif mode == "hard":
            weapons = allWeapons
        else:
            return apology("Please select difficulty")
        
        data = {
            "weapon": weapons[0],
            "lives": 3,
            "hints": 3,
            "current_weapon": 0,
            "current_score": 0,
            "total_weapons": len(weapons)
        }

        # If post requested, restart the game by setting back to default for the sessions:
            # weapons 
            # lives to 3
            # hints to 3
            # total weapons according to the difficulty mode the user selected
            # current weapons back to 0
            # current score back to 0

        session["lives"] = data["lives"]
        session["hints"] = data["hints"]
        session["current_weapon"] = data["current_weapon"]
        session["current_score"] = data["current_score"]
        session["total_weapons"] = data["total_weapons"]

        session["weapons"] = weapons
        session["consecutive_wins"] = 0

        print(session["weapons"][0])
        
        return render_template("public/games/bfv.html", data=data)


@app.route("/bfv/check_results", methods=["POST"])
@login_required
def check_result():
    # Assigning the name of weaon from the input box on the client. 
    weaponNameInput = request.form.get("weaponNameInput").casefold()
    correctWeaponName = session["weapons"][0]["weapon_name"].casefold()

    # Removing the first element within the list (the weapon displayed as an image) 
    # to display the next image within the weapons list
    session["weapons"].pop(0)
    session["current_weapon"] += 1

    if weaponNameInput == correctWeaponName:
        session["current_score"] += 1
        session["consecutive_wins"] += 1
        if session["consecutive_wins"] == 3: 
            # Add 1 more life and hint. Reset sesion consecutive wins back to 0
            session["lives"] += 1
            session["hints"] += 1
            session["consecutive_wins"] = 0

    else:
        session["lives"] -= 1

    print(session["weapons"][0])

    data = {
    "weapon": session["weapons"][0]["encrypted_image_name"],
    "lives": session["lives"],
    "hints": session["hints"],
    "current_weapon": session["current_weapon"],
    "current_score": session["current_score"],
    "total_weapons": session["total_weapons"]
    }

    return jsonify(data)







    # return render_template("public/games/bfv.html", weapons=weapons)

    # Problems:
    # Need to hide name of weapon within img URL
    # Name of weapon in input needs to match with name displayed in the image. 
    # name of weapon should not be visible from client side. 

    # Solutions:
    # Save image as codes (or without name within the name of the image)
    # Instead of getting API through the website, get the API through my database. 
    # Save only the required data from the BF API into the database. 
        # weaponName
        # type
        # maybe image
    # If I can save the type of weapon in the database, I should be able to easily filter out easy, medium and hard weapons. 
    # Also if the BF2042 API gets updated, I can avoid bugs if they updated new weapons, but I haven't saved that image in my webpage. 
