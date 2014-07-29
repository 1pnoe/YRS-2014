"""Using the pokeAPI to compare between different pokemon"""

#Importing the appropriate lib
import requests
import pprint
import json

pokemon_number = raw_input("Please enter pokemon number: ")

#Entry from user on website
pokemon_id = "%s/" % (pokemon_number, )

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

#Iterates through the dictionaries contained within the 'Types' list
def types_function(typ):
    y = []
    for x in typ:
        y.append(str(x["name"]))
    return y

#Pulls the indivitul items from the JSON dictionary and assigns them to variables
name = str(pdict["name"])
national_id = int(pdict["national_id"])
types = str(types_function(pdict["types"]))
attack = int(pdict["attack"])
defense = int(pdict["defense"])
sp_atk = int(pdict["sp_atk"])
sp_def = int(pdict["sp_def"])
speed = int(pdict["speed"])

print


#Puts the JSON variables into a new dictionary
body = {"name": name,
        "national_id": national_id,
        "types": types,
        "attack": attack,
        "defense": defense,
        "sp_atk": sp_atk,
        "sp_def": sp_def,
        "speed": speed}

for key, value in body.items():
    print str(key) + ": " + str(value)

    
