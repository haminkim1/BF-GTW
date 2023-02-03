from flask import render_template, redirect, request, jsonify

from app import app
from modules.apology import apology
from modules.auth_modules import login_required
from modules.get_BF_API import getBFVWeapons

import random

@app.route("/bfv")
@login_required
def bfv_route():

    weapons = getBFVWeapons()

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
            if weapons[i]['weaponName'].casefold().startswith(name.casefold()):
                weaponNames.append(weapons[i]['weaponName'])

        weaponNames = sorted(weaponNames)
        return jsonify(weaponNames)
    else:
        weaponNames = []

    random.shuffle(weapons)

    # send randomized weapon list to query /bfv?submit=
    # submit = request.args.get("submit")


    return render_template("public/games/bfv.html", weapons=weapons)

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
