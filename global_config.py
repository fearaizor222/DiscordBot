import json

global config
global API_Endpoint 

with open('API_Endpoint.json', 'r') as API:
    API_Endpoint = json.load(API)

with open('Config.json', 'r') as file:
    config = json.load(file)