import json
import requests

def Fee(sess: requests.Session()) -> dict:
    with open('API_Endpoint.json', 'r') as API:
        API_Endpoint = json.load(API)

    return sess.post(API_Endpoint['Xem_Hoc_Phi']).json()['data']