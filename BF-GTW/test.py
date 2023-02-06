import os
import hashlib


url = "https://eaassets-a.akamaihd.net/battlelog/battlebinary/gamedata/Casablanca/12/71/MG34-f447ad5e.png"

filename = url.split("/")[-1]

hash = hashlib.sha256(filename.encode()).hexdigest()

print(hash)


x = 1

x -= 1
print(x)