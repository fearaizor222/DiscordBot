from global_config import *
import requests


def RefreshToken(discord_id: str) -> None:
    refresh_token = client['Users'].find_one({'discord_id': discord_id})['refresh_token']
    data = {
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token',
    }
    response = requests.post(API_Endpoint['Login'], data=data, timeout=config['timeout']).json()
    client['Users'].update_one(
        {
            'discord_id': discord_id
        }, 
        {'$set': 
            {
                'access_token': response['access_token'], 
                'refresh_token': response['refresh_token']
            }
        })