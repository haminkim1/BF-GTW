from flask import render_template, request, jsonify

from app import app
from modules.apology import apology
from modules.auth_modules import login_required
from modules.get_weapon_data import get_easy_mode_weapons

# @app.route("/bf1")
# @login_required
# def bf1_route():

#     return render_template("public/games/bf1.html")

@app.route("/bf1")
@login_required
def bf1_route():

    # Was just testing to see if /bfv?name= link would work in this route. 
    # It will work because getting API from that link is related to bfv.js frontend. 
    # weapons = getBFVWeapons()
    # weapons = get_easy_mode_weapons()
    # print(weapons)



    # random.shuffle(weapons)

    # send randomized weapon list to query /bfv?submit=
    # submit = request.args.get("submit")


    # Start this route function anew after creating bfv_weapons table. 
    # But I'll still need the request.args.get("name") and the related codes. 
    # Most likely would need to make modules for selecting weapons in easy, medium and hard modes. 
        # Basically, I just need different SELECT statements depending on the type of the weapons. 
    # Send bfv_weapons table data via API. 
    # Or select db data fro bfv_weapons table within this route and send the data back as a response 
    # Using the data requested via API or this route, use the paste a random image on the page

    














    return render_template("public/games/bf1.html", weapons=weapons)
