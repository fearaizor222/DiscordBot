import json
import requests

def Login(session: requests.Session(), login_data: dict) -> None:
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
        headers = data['headers']
    access_token = session.post(url=API_Endpoint['Login'], headers=headers, data=login_data).json()['access_token']
    auth_headers = headers.copy()
    auth_headers['authorization'] = f'bearer {access_token}'
    session.headers = auth_headers
    # print(cookies)
