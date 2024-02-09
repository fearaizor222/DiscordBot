import json
import requests
import Module.JsonKeyDeletor as JsonKeyDeletor
from global_config import *

def Info(sess: requests.Session()) -> dict:
    info = sess.post(API_Endpoint['Xem_Info'], timeout=config['timeout']).json()
    ma_sv = info['data']['ma_sv']
    image = sess.post(API_Endpoint['Info_Picture'], params=f'MaSV={ma_sv}', timeout=config['timeout']).json()[
        'data']['thong_tin_sinh_vien']['image']
    info['data'].update({'image': "data:image/png;base64," + image})
    info = info['data']

    needed_data = ['ma_sv', 'ten_day_du', 'gioi_tinh', 'ngay_sinh', 'noi_sinh', 'dan_toc', 'ton_giao', 'quoc_tich', 'dien_thoai', 'email', 'dien_thoai2',
                   'email2', 'so_cmnd', 'ho_khau_thuong_tru_gd', 'so_tk', 'lop', 'khu_vuc', 'doi_tuong_uu_tien', 'khoi', 'nganh', 'chuyen_nganh', 'khoa',
                   'ba_he_dao_tao', 'nien_khoa', 'ma_truong', 'ten_truong', 'nhhk_vao', 'nhhk_ra', 'hien_dien_sv', 'image']

    JsonKeyDeletor(info, needed_data)

    return info
