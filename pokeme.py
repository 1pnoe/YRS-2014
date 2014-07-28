"""Using the pokeAPI to compare between different pokemon"""

#Importing the appropriate lib

import requests


body = {"name": name,
        "national_id": national_id,
        "types": types,
        "attack": attack,
        "defence": defence,
        "sp_atk": sp_atk,
        "sp_def": sp_def,
        "speed": speed,
        "total": total}

response = requests.post("http://pokeapi.co/api/v1/pokemon/", 
