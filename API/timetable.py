import requests
from Module import jsonKeyDeletor
from global_configuration import *

def requestTimetable(sess: requests.Session, semester: int) -> dict:
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

    data = sess.post(ENDPOINT['Xem_Lich_Hoc'],
                     headers=special_headers, json=json_data, timeout=CONFIG['timeout']).json()['data']
    tkb_hk = data.pop('ds_tuan_tkb')

    needed_data = [
        'tuan_tuyet_doi',
        'tuan_hoc_ky',
        'thong_tin_tuan',
        'ngay_bat_dau',
        'ngay_ket_thuc',
        'ds_thoi_khoa_bieu',
        'tiet_bat_dau',
        'so_tiet',
        'ma_mon',
        'ten_mon',
        'ten_giang_vien',
        'ma_phong',
        'ngay_hoc'
    ]

    jsonKeyDeletor(tkb_hk, needed_data)

    return tkb_hk
