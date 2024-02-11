from global_configuration import *
import requests

def refreshToken(discord_id: str) -> None:
    refresh_token = CLIENT['Users'].find_one({'discord_id': discord_id})['refresh_token']
    data = {
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token',
    }
    response = requests.post(ENDPOINT['Login'], data=data, timeout=CONFIG['timeout']).json()
    CLIENT['Users'].update_one(
        {
            'discord_id': discord_id
        }, 
        {'$set': 
            {
                'access_token': response['access_token'], 
                'refresh_token': response['refresh_token']
            }
        })