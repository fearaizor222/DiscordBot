import json
import requests

def Info(sess: requests.Session()) -> dict:
    with open('API_Endpoint.json', 'r') as API:
        API_Endpoint = json.load(API)
    
    info = sess.post(API_Endpoint['Xem_Info']).json()
    ma_sv = info['data']['ma_sv']
    image = sess.post(API_Endpoint['Info_Picture'], params=f'MaSV={ma_sv}').json()['data']['thong_tin_sinh_vien']['image']
    info['data'].update({'image': "data:image/png;base64," + image})
    return info['data']