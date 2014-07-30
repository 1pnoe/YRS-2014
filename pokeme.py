"""Using the pokeAPI to compare between different pokemon"""

#Importing the appropriate lib
import requests
import pprint
import json

pokemon_number_1 = raw_input("Please enter pokemon number: ")

#Entry from user on website
pokemon_id_1 = "%s/" % (pokemon_number_1, )

#The URL of the API
endpoint_1 = "http://pokeapi.co/api/v1/pokemon/"

#Requesting a response from the API using the given "pokemon_id"
response_1 = requests.get( endpoint_1 + pokemon_id_1, )

#Printing the url given by the API
print response_1.url
print response_1.status_code
print "-------------------------------------------------"

#variable which stores that data from the API request
data_1= response_1.content

#Converting the JSON dictionary into a Python dictionary
pdict_1 = json.loads(str(data_1))

#Iterates through the dictionaries contained within the 'Types' list
def types_function_1(typ):
    y = []
    for x in typ:
        y.append(str(x["name"]))
    return y

#Pulls the indivitul items from the JSON dictionary and assigns them to variables
name_1 = str(pdict_1["name"])
national_id_1 = int(pdict_1["national_id"])
types_1 = str(types_function_1(pdict_1["types"]))
attack_1 = int(pdict_1["attack"])
defense_1 = int(pdict_1["defense"])
sp_atk_1 = int(pdict_1["sp_atk"])
sp_def_1 = int(pdict_1["sp_def"])
speed_1 = int(pdict_1["speed"])
hp_1 = int(pdict_1["hp"])
average_1 = int((attack_1 + defense_1 + sp_atk_1 + sp_def_1 + speed_1 + hp_1) / 6)

#Puts the JSON variables into a new dictionary
body_1 = {"name": name_1,
        "national_id": national_id_1,
        "types": types_1,
        "attack": attack_1,
        "defense": defense_1,
        "sp_atk": sp_atk_1,
        "sp_def": sp_def_1,
        "speed": speed_1,
        "hp": hp_1,
        "average": average_1}

for key, value in body_1.items():
    print str(key) + ": " + str(value)

print "-------------------------------------------------"

pokemon_number_2 = raw_input("Please enter the second pokemon number: ")

pokemon_id_2 = "%s/" % (pokemon_number_2, )

endpoint_2 = "http://pokeapi.co/api/v1/pokemon/"

response_2 = requests.get( endpoint_2 + pokemon_id_2, )
print response_1.url
print response_1.status_code

print "-------------------------------------------------"

data_2= response_2.content

pdict_2 = json.loads(str(data_2))

def types_function_2(typ):
    y = []
    for x in typ:
        y.append(str(x["name"]))
    return y

name_2 = str(pdict_2["name"])
national_id_2 = int(pdict_2["national_id"])
types_2 = str(types_function_2(pdict_2["types"]))
attack_2 = int(pdict_2["attack"])
defense_2 = int(pdict_2["defense"])
sp_atk_2 = int(pdict_2["sp_atk"])
sp_def_2 = int(pdict_2["sp_def"])
speed_2 = int(pdict_2["speed"])
hp_2 = int(pdict_2["hp"])
average_2 = int((attack_2 + defense_2 + sp_atk_2 + sp_def_2 + speed_2 + hp_2) / 6)

body_2 = {"name": name_2,
        "national_id": national_id_2,
        "types": types_2,
        "attack": attack_2,
        "defense": defense_2,
        "sp_atk": sp_atk_2,
        "sp_def": sp_def_2,
        "speed": speed_2,
        "hp": hp_2,
        "average": average_2}

for key, value in body_2.items():
    print str(key) + ": " + str(value)

print "-------------------------------------------------"


stats_array = [
    [1,1,1,1,1,1,1,1,1,1,1,1,0.5,0,1,1,0.5,1]
    [1,0.5,0.5,1,2,2,1,1,1,1,1,2,0.5,1,0.5,1,2,1]
    [1,2,0.5,1,035,1,1,1,2,1,1,1,2,1,035,1,1,1]
    [1,1,2,0.5,0.5,1,1,1,0,2,1,1,1,1,0.5,1,1,1]
    [1,0.5,2,1,0.5,1,1,0.5,2,0.5,1,0.5,2,1,0.5,1,0.5,1]
    [1,0.5,0.5,1,2,0.5,1,1,2,2,1,1,1,1,2,1,0.5,1]
    [2,1,1,1,1,2,1,0.5,1,0.5,0.5,0.5,2,0,1,2,2,0.5]
    [2,1,1,1,1,2,1,0.5,1,0.5,0.5,0.5,2,0,1,2,2,0.5]
    [1,2,1,2,0.5,1,1,2,1,0,1,0.5,2,1,1,1,2,1]
    [1,1,1,0.5,2,1,2,1,1,1,1,2,0.5,1,1,1,0.5,1]

average_difference = abs(average_1-average_2)

if average_1 > average_2:
    print ("%s beats %s with a average point differnce of %s" % (name_1, name_2, str(average_difference), ))
elif average_1 < average_2:
    print ("%s beats %s with a average point differnce of %s" % (name_2, name_1, str(average_difference), ))
else:
    print ("Stalemate! Both %s and %s have the same average point score" % (name_1, name_2, ))
    

