import json
import requests
from global_config import *

def Login(session: requests.Session(), login_data: dict) -> str:
    """
    Login to UIS system
    :param session: Session to use
    :param login_data: Login data
    :return: None
    """
    session_data = session.post(url=API_Endpoint['Login'], data=login_data, timeout=config['timeout']).json()
    session.headers['authorization'] = f'bearer {session_data["access_token"]}'
    return session_data['refresh_token']