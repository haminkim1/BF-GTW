from app.db.db_config import db

import random

def get_all_weapons():
    weapons = db.execute("SELECT * FROM bfv_weapons ORDER BY weapon_name")
    return weapons

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


def get_hard_mode_weapons(weapons):
    hardWeapons = weapons
    return hardWeapons


def get_first_easy_weapon():
    while True:
        weapon = db.execute("SELECT * FROM bfv_weapons ORDER BY RANDOM() LIMIT 1")
        if weapon[0]["weapon_type"] != "Melee" and weapon[0]["weapon_type"] != "Gadget" and weapon[0]["weapon_type"] != "Sidearm":
            break
    return weapon


def get_test_weapon():
    weapons = db.execute("SELECT * FROM bfv_weapons ORDER BY weapon_name DESC LIMIT 4")
    return weapons