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
        weaponNames = []
        # If value of name key exists, cycle through each weapon name. 
        # If the weapon names start with name, append only the weapon name (not the entire object) to weaponNames list. 
        # Return weaponNames as JSON data back as a response to the client. 
        if name:
            for i in range(len(weapons)):
                # I'll need an IF statement where if name == first letters of each list, then return jsonify those names only
                # Make sure to return alphabetically
                if weapons[i]['weapon_name'].casefold().startswith(name.casefold()):
                    weaponNames.append(weapons[i]['weapon_name'])

            weaponNames = sorted(weaponNames)
            return jsonify(weaponNames)
        else:
            weaponNames = []

        return render_template("public/games/bfv.html", weapons=weapons, lives=lives, hints=hints, weapon=weapon)

    else:
        # If post requested, restart the game. 
        # If post request made, clears the weapons session first to reset the game. 
        # session.pop("weapons", None)
        # session.pop("lives", None)
        # session.pop("hints", None)
        # Not sure if I need to add these pop sessions when the codes below would do that anyway upon post request. 
        
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
            "lives": 3,
            "hints": 3,
            "total_weapons": len(weapons),
            "current_weapon": 0,
            "current_score": 0
        }

        session["weapons"] = weapons
        session["lives"] = data["lives"]
        session["hints"] = data["hints"]
        session["total_weapons"] = data["total_weapons"]
        session["current_weapon"] = data["current_weapon"]
        session["current_score"] = data["current_score"]

        print(session["weapons"][0])
        
        return render_template("public/games/bfv.html", weapons=weapons, data=data)


        # Create a form that sends a post request to a different URL (eg /bfv/check_results)
        # If submit button clicked,
            # send request input value to server
            # send request value of lives and hints to server
        
        # If session["lives"] and "hints" != value of lives and hints, return apology "Stop cheating"
        # Actually no need to send lives and hints, when those values are stored under the session anyway.
        # I will just have to subtract or add the values depending on the results and return it back to the client. 

        # If input.value != weapons[0]["weapon_name"]
            # session["lives"] - 1
        
        # Remove first index of weapons
        
        # Render template with weapons, lives and hints back to client. 

        # Main problem: How do I compare input.value and weapon[0]["weapon_name"]. 
            # if session["weapons"][0]["weapon_name"] != input.value?

@app.route("/bfv/check_results", methods=["POST"])
@login_required
def check_result():
    print(request.form.get("weaponNameInput"))

    weaponNameInput = request.form.get("weaponNameInput").casefold()
    correctWeaponName = session["weapons"][0]["weapon_name"].casefold()

    session["weapons"].pop(0)

    weapon = session["weapons"][0]
    lives = session["lives"]

    if weaponNameInput == correctWeaponName:
        # if session["current_score"] % 3: add 1 more life. 
        print("placeholder")
    else:
        lives = lives - 1
    
    return jsonify(weapon, lives)


@app.route("/test", methods=["GET", "POST"])
@login_required
def testing():

    if request.method == "POST":
        return redirect("/bfv")





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

@app.route("/bfv/submit")
@login_required
def bfv_submit():

    return redirect("/bfv")
