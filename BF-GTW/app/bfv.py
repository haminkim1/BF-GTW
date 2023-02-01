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

    # I need an alphabetically sorted weapons name list. 
    name = request.args.get("name")
    weaponsName = []
    if name:
        for i in range(len(weapons)):
            # I'll need an IF statement where if name == first letters of each list, then return jsonify those names only
            # Make sure to return alphabetically
            weaponsName.append(weapons[i]['weaponName'])
            # print(weaponsName)
        print(name)
        return jsonify(weaponsName)
    else:
        weaponsName = []

    random.shuffle(weapons)

    return render_template("public/games/bfv.html", weapons=weapons)

