"""Using the pokeAPI to compare between different pokemon"""

#Importing the appropriate lib

import requests
import pprint
import json

################################################
"""
name = ""
national_id = ""
types = ""
attack = ""
defence = ""
sp_atk = ""
sp_def = ""
speed = ""
total = ""
"""

"""
body = {"name": name,
        "national_id": national_id,
        "types": types,
        "attack": attck,
        "defence": defence,
        "sp_atk": sp_atk,
        "sp_def": sp_def,
        "speed": speed,
        "total": total}
"""
################################################




#Entry from user on website
pokemon_id = "1/"

#The URL of the API
endpoint = "http://pokeapi.co/api/v1/pokemon/"

#Requesting a response from the API using the given "pokemon_id"
response = requests.get( endpoint + pokemon_id, )

#Printing the url given by the API
url = response.url
print (url)

#variable which stores that data from the API request
data= response.content

#Converting the JSON dictionary into a Python dictionary
var = json.loads(str(data))

"""
for item in data:
    print (item)
"""

#Fetches the name of the first ability in the "1" pokemon dictionary
pprint.pprint(var["abilities"][1]["name"])

