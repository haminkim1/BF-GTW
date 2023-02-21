from flask import jsonify, render_template, request, session

from app import app
from modules.apology import apology
from modules.auth_modules import login_required
from modules.games_modules import data_for_next_round, game_over, initialize_games_data, reset_games_sessions, return_hint_data, save_game_data
from modules.get_weapon_data import get_all_weapons, get_easy_mode_weapons, get_first_easy_weapon, get_hard_mode_weapons, get_medium_mode_weapons, get_test_weapon

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
        elif mode == "test":
            weapons = get_test_weapon()
        else:
            return apology("Please select difficulty")
        
        random.shuffle(weapons)
        session["weapons"] = weapons

        if mode == "easy" or mode == "medium" or mode == "hard" or mode == "test":
            session["play_state"] = True
            play_state = session["play_state"]


        data = initialize_games_data(weapons)

        # If post requested, restart the game by setting back to default for the sessions:
            # weapons 
            # lives to 3
            # hints to 3
            # total weapons according to the difficulty mode the user selected
            # current weapons back to 0
            # current score back to 0
            # consecutive wins back to 0

        reset_games_sessions(data, mode, "bfv")

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
        round = "win"
        session["current_score"] += 1
        session["consecutive_wins"] += 1
        if session["consecutive_wins"] == 3: 
            # Add 1 more life and hint. Reset session consecutive wins back to 0
            session["consecutive_wins"] = 0
            session["lives"] += 1
            session["hints"] += 1
    else:
        round = "lose"
        session["lives"] -= 1

    previousWeaponName = session["weapons"][index_no]["weapon_name"]
    session["current_weapon"] += 1

    # If current weapon is less than total weapons, game is not over
    # Else, all the weapon has been cycled through and user has won the game
    if session["current_weapon"] < session["total_weapons"]:
        # Setting index number to the current weapon number.
        # This will send the next element in session["weapons"] and proceed with the next guessing round.
        index_no = session["current_weapon"]

    print(session["weapons"][index_no])
    data = data_for_next_round(index_no, round, previousWeaponName)
    
    # If game over, set play state to false. 
    if data["current_weapon"] == data["total_weapons"] or data["lives"] == 0:
        save_game_data()
        game_over()
    return jsonify(data)


@app.route("/bfv/hint", methods=["POST"])
@login_required
def hint():
    data = {}
    
    if session["hints"] > 0:
        session["hints"] -= 1
        data = return_hint_data()

    return jsonify(data)


