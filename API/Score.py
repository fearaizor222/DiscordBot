import json
import requests

def Score(sess: requests.Session()) -> dict:
    with open('API_Endpoint.json', 'r') as API:
        API_Endpoint = json.load(API)
    
    return sess.post(API_Endpoint['Xem_Diem']).json()['data']