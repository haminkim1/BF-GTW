import json
import requests
import os


# Getting API data. 
response_API = requests.get('https://api.gametools.network/bfv/weapons/?format_values=true&name=HAMINATOR1997&platform=pc&skip_battlelog=false&lang=en-us')
data = response_API.text
# Converting API data into JSON. 
jsonData = json.loads(data)

# Assigning only weapons data into weapon variable
jsonDataWeapons = jsonData["weapons"]
easyModeWeapons = []
imageLinks = []
counter = 0
cwd = os.getcwd()

# Taking out melee, gadget and sidearm weapons. 
# Taking out melee, gadget and sidearm weapons. 
for i in range(len(jsonDataWeapons)):
    if jsonDataWeapons[i]["type"] != "Melee" and jsonDataWeapons[i]["type"] != "Gadget" and jsonDataWeapons[i]["type"] != "Sidearm":
        easyModeWeapons.append(jsonDataWeapons[i])
        imageLinks.append(jsonDataWeapons[i]["image"])

for url in imageLinks:

    response = requests.get(url)

    if response.status_code == 200:
        # filename = url.split("/")[-1]
        counter += 1
        filename = str("{}.png".format(counter))

        save_path = os.path.join(cwd, filename)

        with open(save_path, "wb") as f:
            f.write(response.content)
        
        print(f"Successfully saved {filename} to {cwd}")
    else:
        print(f"Failed to download")