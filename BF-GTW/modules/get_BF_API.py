import requests
import json

# Exclude types:
# melee
# gadget
# sidearm

# Only include dictionaries within weapons dictionary:
# weaponName
# type
# image

def getBFVWeapons():
    # Getting API data. 
    response_API = requests.get('https://api.gametools.network/bfv/weapons/?format_values=true&name=HAMINATOR1997&platform=pc&skip_battlelog=false&lang=en-us')
    data = response_API.text
    # Converting API data into JSON. 
    jsonData = json.loads(data)

    # Assigning only weapons data into weapon variable
    jsonDataWeapons = jsonData["weapons"]
    weapons = []

    # Taking out melee, gadget and sidearm weapons. 
    for i in range(len(jsonDataWeapons)):
        if jsonDataWeapons[i]["type"] != "Melee" and jsonDataWeapons[i]["type"] != "Gadget" and jsonDataWeapons[i]["type"] != "Sidearm":
            weapons.append(jsonDataWeapons[i])

    return weapons