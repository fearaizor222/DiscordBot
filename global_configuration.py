import json
from pymongo import MongoClient

global CONFIG
global ENDPOINT
global CLIENT

with open('endpoint.json', 'r') as API:
    ENDPOINT = json.load(API)

with open('configuration.json', 'r') as file:
    CONFIG = json.load(file)

CLIENT = MongoClient(CONFIG['database'])['UIS']