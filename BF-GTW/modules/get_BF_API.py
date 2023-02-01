import requests
import json

response_API = requests.get('https://api.gametools.network/bfv/weapons/?format_values=true&name=HAMINATOR1997&platform=pc&skip_battlelog=false&lang=en-us')
print(response_API)

data = response_API.text
# print (data)

json.loads(data)

jsonData = json.loads(data)

mg42 = jsonData["weapons"][0]["image"]

print(mg42)