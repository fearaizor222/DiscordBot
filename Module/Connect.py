from pymongo import MongoClient, database
import json

def Connect(database_name: str) -> database.Database:
    with open('Additional_Data.json', 'r') as AD:
        data = json.load(AD)
        connection_string = data['database']

    client = MongoClient(connection_string)
    return client[database_name]