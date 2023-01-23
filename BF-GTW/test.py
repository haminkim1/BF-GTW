import requests
headers = {'TRN-Api-Key' :'c8288c3c-1d53-407a-926c-0e851d083a02'}
username = 'HAMINATOR1997'
BASIC_STATS_URL = 'https://api.gametools.network/bfv/weapons/?format_values=true&name={}&platform=pc&skip_battlelog=false&lang=en-us'
r = requests.get(BASIC_STATS_URL.format(username), headers=headers)

test = r.json()
print(test["avatar"])
print(test["weapons"][0]["weaponName"])

response = requests.get("http://randomfox.ca/floof")
fox = response.json()
print(fox["image"])


# print()
