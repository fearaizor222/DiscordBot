import requests
from global_configuration import *

def requestLogin(session: requests.Session, login_data: dict) -> str:
    """
    Login to UIS system
    :param session: Session to use
    :param login_data: Login data
    :return: None
    """
    session_data = session.post(url=ENDPOINT['Login'], data=login_data, timeout=CONFIG['timeout']).json()
    session.headers['authorization'] = f'bearer {session_data["access_token"]}'
    return session_data['access_token'], session_data['refresh_token']