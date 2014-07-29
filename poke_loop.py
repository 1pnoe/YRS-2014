import requests
import pprint
import json
import time

def pokemon_id(number):
    id = "%s/" % (number, )
    return str(id)

endpoint = "http://pokeapi.co/api/v1/pokemon/"

def id_loop():
    for i in range(1, 718):
        response = requests.get(endpoint + (pokemon_id(i)))
        data = response.content
        print response.status_code
        pdict = json.loads(str(data))
        print str(pdict["national_id"])
        print str(pdict["name"])
        time.sleep(0.5)
        

id_loop()
