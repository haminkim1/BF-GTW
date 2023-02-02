from flask import render_template, request, jsonify

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

    return render_template("public/games/bfv.html", weapons=weapons)

