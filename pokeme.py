"""Using the pokeAPI to compare between different pokemon"""

#Importing the appropriate lib

import requests
import pprint

name = ""
national_id = ""
types = ""
attack = ""
defence = ""
sp_atk = ""
sp_def = ""
speed = ""
total = ""

#body = {"name": name,
 #       "national_id": national_id,
  #      "types": types,
   #     "attack": attack,
    #    "defence": defence,
     #   "sp_atk": sp_atk,
      #  "sp_def": sp_def,
       # "speed": speed,
        #"total": total}

#Entry from user on website
pokemon_id = "1/"

#The URL of the API
endpoint = "http://pokeapi.co/api/v1/pokemon/"

#Requesting a response from the API using the given "pokemon_id"
response = requests.get( endpoint, params=pokemon_id)

#variable which stores that data from the API request
data= response.json

pprint.pprint(data)

print (data.name)
