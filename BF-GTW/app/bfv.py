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
            alphabeticallySortedName = sorted(weapons) #This is not sorting because I need to sort weapons[i]["weapon_name"], not the weapons object itself. 
            alphabeticallySortedName = weapons

            for i in range(len(alphabeticallySortedName)):
                if weapons[i]['weapon_name'].casefold().startswith(name.casefold()):
                    startingPoint = alphabeticallySortedName[i:]
                    break
            # Sort list alphabetically
            # If weapon name starts with name:
                # Start from that index. 
                # If no weapons found afterwards
                    # break
            for i in range(len(startingPoint)):
                # If name == first letters of each list, return names as JSON object alphabetically
                if startingPoint[i]['weapon_name'].casefold().startswith(name.casefold()):
                    weaponNames.append(startingPoint[i]['weapon_name'])
                else:
                    break
            
            # Sorting the list alphabetically
            weaponNames = sorted(weaponNames)
            return jsonify(weaponNames)
        else:
            weaponNames = []

        session["play_state"] = False

        return render_template("public/games/bfv.html", weapons=weapons, lives=lives, hints=hints, weapon=weapon)

    else:       
        mode = request.form.get("mode")
        print(mode)
        if mode == "easy":
            weapons = get_easy_mode_weapons(allWeapons)
        elif mode == "medium":
            weapons = get_medium_mode_weapons(allWeapons)
        elif mode == "hard":
            weapons = allWeapons
        else:
            return apology("Please select difficulty")
        
        if mode == "easy" or mode == "medium" or mode == "hard":
            session["play_state"] = True
            play_state = session["play_state"]
        
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
        
        return render_template("public/games/bfv.html", data=data, play_state=play_state)


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


# Make user press start button before playing the game
# Create session["play_state"] = false when get requested on /bfv
# If one of the modes clicked and submitted, set sesion["play_state"] to true
# If false, set submit button to start
# If true, set submit button to true