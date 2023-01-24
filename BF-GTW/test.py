import requests
# headers = {'TRN-Api-Key' :'c8288c3c-1d53-407a-926c-0e851d083a02'}
# username = 'HAMINATOR1997'
# BASIC_STATS_URL = 'https://api.gametools.network/bfv/weapons/?format_values=true&name={}&platform=pc&skip_battlelog=false&lang=en-us'
# r = requests.get(BASIC_STATS_URL.format(username), headers=headers)

# test = r.json()
# print(test["avatar"])
# print(test["weapons"][0]["weaponName"])

# response = requests.get("http://randomfox.ca/floof")
# fox = response.json()
# print(fox["image"])


# print()

# import requests


# Your API key and username
api_key = "c8288c3c-1d53-407a-926c-0e851d083a02"
username = "HAMINATOR1997"
platform = "origin"

# Set the headers for the request
headers = {
    "TRN-Api-Key": api_key
}

# Set the parameters for the request
params = {
    "platform": platform,
    "username": username
}

# Make the GET request to the API
response = requests.get("https://api.tracker.gg/v2/bfv/standard-profile", headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    print(data)
else:
    print(f"Error {response.status_code}: {response.text}")
