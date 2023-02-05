import requests
import json

from app.db.db_config import db

# Exclude types:
# melee
# gadget
# sidearm

# Only include dictionaries within weapons dictionary:
# weaponName
# type
# image




def get_easy_mode_weapons(weapons):

    easyWeapons = []
    # Taking out melee, gadget and sidearm weapons. 
    for i in range(len(weapons)):
        if weapons[i]["weapon_type"] != "Melee" and weapons[i]["weapon_type"] != "Gadget" and weapons[i]["weapon_type"] != "Sidearm":
            easyWeapons.append(weapons[i])


    return easyWeapons


def get_medium_mode_weapons(weapons):
    mediumWeapons = []
    # Taking out melee, gadget and sidearm weapons. 
    for i in range(len(weapons)):
        if weapons[i]["weapon_type"] != "Gadget":
            mediumWeapons.append(weapons[i])


    return mediumWeapons


def get_hard_mode_weapons():
    weapons = db.execute("SELECT * FROM bfv_weapons")
    return weapons
