"""Using the pokeAPI to compare between different pokemon"""

#Importing the appropriate lib
import requests
import pprint
import json

#Entry from user on website
pokemon_id = "1/"

#The URL of the API
endpoint = "http://pokeapi.co/api/v1/pokemon/"

#Requesting a response from the API using the given "pokemon_id"
response = requests.get( endpoint + pokemon_id, )

#Printing the url given by the API
print response.url
print response.status_code
print "-------------------------------------------------"

#variable which stores that data from the API request
data= response.content

#Converting the JSON dictionary into a Python dictionary
pdict = json.loads(str(data))

#Fetches the name of the first ability in the "1" pokemon dictionary
#name =(pdict["abilities"][1]["name"])

"""
for x in pdicts["types"]:
    return x["name"]
"""

def types_function(typ):
    y = []
    for x in typ:
        y.append(x["name"])
    return y

name = str(pdict["name"])
national_id = str(pdict["national_id"])
types = types_function(pdict["types"])
attack = str(pdict["attack"])
defense = str(pdict["defense"])
sp_atk = str(pdict["sp_atk"])
sp_def = str(pdict["sp_def"])
speed = str(pdict["speed"])
total = str(pdict["total"])

print types
 


body = {"name": name,
        "national_id": national_id,
        "types": types,
        "attack": attack,
        "defense": defense,
        "sp_atk": sp_atk,
        "sp_def": sp_def,
        "speed": speed,
        "total": total}

print body 
