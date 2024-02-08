import requests
import Module.JsonKeyDeletor as JsonKeyDeletor
import json


def ExamSchedule(sess: requests.Session, semester: int) -> dict:
    with open('API_Endpoint.json', 'r') as API:
        API_Endpoint = json.load(API)
    with open('Additional_Data.json', 'r') as AD:
        data = json.load(AD)

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

    data = sess.post(API_Endpoint['Xem_Lich_Thi'],
                     headers=special_headers, json=json_data,timeout=data['timeout']).json()['data']
    ds_lichthi = data['ds_lich_thi']
    needed_data = ['so_thu_tu', 'ky_thi', 'ma_mon', 'ten_mon', 'ma_phong', 'ngay_thi',
                   'tiet_bat_dau', 'so_tiet', 'gio_bat_dau', 'so_phut', 'hinh_thuc', 'si_so']

    JsonKeyDeletor(ds_lichthi, needed_data)

    return ds_lichthi