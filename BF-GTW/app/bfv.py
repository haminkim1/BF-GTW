from flask import jsonify, redirect, render_template, request, session

from app import app
from modules.apology import apology
from modules.auth_modules import login_required
from modules.get_weapon_data import get_easy_mode_weapons, get_first_easy_weapon, get_hard_mode_weapons, get_medium_mode_weapons

import random

@app.route("/bfv", methods=["GET", "POST"])
@login_required
def bfv_route():
    allWeapons = get_hard_mode_weapons()
    weapon = get_first_easy_weapon(allWeapons)

    if request.method == "GET":
        # Getting hard mode weapons is pretty much retrieving every single weapon in the db. 
        weapons = session.get("weapons", [])

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

        return render_template("public/games/bfv.html", weapons=weapons, weapon=weapon)

    else:
        # If post requested, restart the game. 
        # If post request made, clears the weapons session first to reset the game. 
        session.pop("weapons", None)
        
        mode = request.form.get("mode")
        if mode == "easy":
            weapons = get_easy_mode_weapons(allWeapons)
            print(mode)
        elif mode == "medium":
            weapons = get_medium_mode_weapons(allWeapons)
            print(mode)
        elif mode == "hard":
            weapons = allWeapons
            print(mode)
        else:
            return apology("Please select difficulty")

        session["weapons"] = weapons
        print(session["weapons"][0])
        
        return render_template("public/games/bfv.html", weapons=weapons)











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
