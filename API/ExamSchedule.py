import requests
import json

def ExamSchedule(sess: requests.Session, semester: int) -> dict:
    with open('API_Endpoint.json', 'r') as API:
        API_Endpoint = json.load(API)

    json_data = {
        'filter': {
            'hoc_ky': semester,
            'ten_hoc_ky': '',
        },
        'additional': {
            'paging': {
                'limit': 100,
                'page': 1,
            },
            'ordering': [
                {
                    'name': None,
                    'order_type': None,
                },
            ],
        },
    }
    special_headers = sess.headers.copy()
    special_headers['content-type'] = 'application/json'

    return sess.post(API_Endpoint['Xem_Lich_Thi'], headers=special_headers, json=json_data).json()['data']