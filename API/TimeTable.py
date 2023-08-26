import json
import requests

def TimeTable(sess: requests.Session(), semester: int) -> dict:
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

    data = sess.post(API_Endpoint['Xem_Lich_Hoc'], headers=special_headers, json=json_data).json()['data']
    tkb_hk = data.pop('ds_tuan_tkb')

    needed_data = [
        'tiet_bat_dau',
        'so_tiet',
        'ma_mon',
        'ten_mon',
        'ten_giang_vien',
        'ma_phong',
        'ngay_hoc' 
    ]
    for week in tkb_hk:
        week.pop('ds_id_thoi_khoa_bieu_trung', None)
        for day in week['ds_thoi_khoa_bieu']:
            for key in list(day):
                if key not in needed_data:
                    day.pop(key, None)

    return tkb_hk
