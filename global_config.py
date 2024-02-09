import json
from pymongo import MongoClient, errors

global config
global API_Endpoint 
global client

with open('API_Endpoint.json', 'r') as API:
    API_Endpoint = json.load(API)

with open('Config.json', 'r') as file:
    config = json.load(file)

client = MongoClient(config['database'])['UIS']