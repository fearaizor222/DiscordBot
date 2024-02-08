import json
import requests

def Login(session: requests.Session(), login_data: dict) -> str:
    """
    Login to UIS system
    :param session: Session to use
    :param login_data: Login data
    :return: None
    """
    with open('API_Endpoint.json', 'r') as API:
        API_Endpoint = json.load(API)

    with open('Additional_Data.json', 'r') as AD:
        data = json.load(AD)
    session_data = session.post(url=API_Endpoint['Login'], data=login_data, timeout=data['timeout']).json()
    session.headers['authorization'] = f'bearer {session_data["access_token"]}'
    return session_data['refresh_token']