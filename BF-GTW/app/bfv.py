from flask import jsonify, redirect, render_template, request, session

from app import app
from modules.apology import apology
from modules.auth_modules import login_required
from modules.get_weapon_data import get_all_weapons, get_easy_mode_weapons, get_first_easy_weapon, get_hard_mode_weapons, get_medium_mode_weapons

import random 

@app.route("/bfv", methods=["GET", "POST"])
@login_required
def bfv_route():   
    if request.method == "GET":

        weapon = get_first_easy_weapon()
        session["play_state"] = False

        return render_template("public/games/bfv.html", weapon=weapon[0])

    else:       
        # Getting hard mode weapons is pretty much retrieving every single weapon in the db. 
        allWeapons = get_all_weapons()

        mode = request.form.get("mode")
        if mode == "easy":
            weapons = get_easy_mode_weapons(allWeapons)
        elif mode == "medium":
            weapons = get_medium_mode_weapons(allWeapons)
        elif mode == "hard":
            weapons = get_hard_mode_weapons(allWeapons)
        else:
            return apology("Please select difficulty")
        
        random.shuffle(weapons)
        session["weapons"] = weapons

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
        session["consecutive_wins"] = 0

        print(session["weapons"][0])
        
        return render_template("public/games/bfv.html", data=data, play_state=play_state)


@app.route("/bfv/name")
@login_required
def list_bfv_weapons():
    weapons = session["weapons"]
    # Get query parameter of key called "name"
    name = request.args.get("name")

    if name:
        weaponNames = []
        # Think about using while loops instead. 
        # Still need an alphabetically sorted list. 
        # Even if app is not optimal due to moving the name API into a separate route,
        # don't delete the while loop comments yet as I can still potentially increase
        # more efficiency using while loop. 
        # I just need to somehow bring an alphabetically sorted weapons list. 
        # While weapons[i]["weapon_name"] != name or i < len(list)
            # i++
        # if == name, then [i:] to a new list. 
        for i in range(len(weapons)):
            if weapons[i]['weapon_name'].casefold().startswith(name.casefold()):
                weaponNames.append(weapons[i]['weapon_name'])
        
        # While new_list[i:] == name
            # append. 
            # i++
        # If != name, then exit while loop. 
                
        # Sorting the list alphabetically
        weaponNames = sorted(weaponNames)

    else:
        weaponNames = []
    return jsonify(weaponNames)


@app.route("/bfv/check_results", methods=["POST"])
@login_required
def check_result():
    # Assigning the name of weaon from the input box on the client. 
    index_no = session["current_weapon"]
    weaponNameInput = request.form.get("weaponNameInput").casefold()
    correctWeaponName = session["weapons"][index_no]["weapon_name"].casefold()

    if weaponNameInput == correctWeaponName:
        session["current_score"] += 1
        session["consecutive_wins"] += 1
        if session["consecutive_wins"] == 3: 
            # Add 1 more life and hint. Reset session consecutive wins back to 0
            session["consecutive_wins"] = 0
            session["lives"] += 1
            session["hints"] += 1
            
    else:
        session["lives"] -= 1

    # Setting index number to the current weapon number.
    # This will send the next element in session["weapons"] and proceed with the next guessing round.
    session["current_weapon"] += 1
    index_no = session["current_weapon"]
    print(session["weapons"][index_no])

    data = {
    "weapon": session["weapons"][index_no]["encrypted_image_name"],
    "lives": session["lives"],
    "hints": session["hints"],
    "current_weapon": session["current_weapon"],
    "current_score": session["current_score"],
    "total_weapons": session["total_weapons"]
    }

    return jsonify(data)


@app.route("/bfv/hint", methods=["POST"])
@login_required
def hint():
    data = {}
    index_no = session["current_weapon"]
    # Do nothing if user clicks hints button but there are no hints left. 
    if session["hints"] == 0:
        data["hints"] = session["hints"]
        return jsonify(data)
    else:
        session["hints"] -= 1
        # Getting first letter of weapon name. 
        first_letter = session["weapons"][index_no]["weapon_name"][0]
        data = {
            "hints": session["hints"],
            "weapon_type": session["weapons"][index_no]["weapon_type"],
            "first_letter": first_letter
        }
        return jsonify(data)



