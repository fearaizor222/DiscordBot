from Module import jsonKeyDeletor
import requests
from global_configuration import *

def requestScore(sess: requests.Session) -> dict:
    data = sess.post(ENDPOINT['Xem_Diem'], timeout=CONFIG['timeout']).json()['data']['ds_diem_hocky']

    # dsdiemhk = sess.post(API_Endpoint['Xem_Diem']).json()['data']['ds_diem_hocky'][4]
    needed_data = ['hoc_ky', 'ten_hoc_ky', 'so_tin_chi_dat_tich_luy', 'so_tin_chi_dat_hk', 'ds_diem_mon_hoc', 'dtb_hk_he10', 'dtb_hk_he4', 'dtb_tich_luy_he_10',
                   'dtb_tich_luy_he_4', 'ma_mon', 'nhom_to', 'ten_mon', 'so_tin_chi', 'diem_thi', 'diem_giua_ki', 'diem_tk', 'diem_tk_so', 'diem_tk_chu', 'ds_diem_thanh_phan']

    # for obj in data:

    #     for element in list(obj):
    #         if element not in needed_obj:
    #             obj.pop(element,None)
    #             continue
    #         data1= data[stt]['ds_diem_mon_hoc']
    #         if element == 'ds_diem_mon_hoc':
    #             for i in data1:
    #                 for key in list(i):
    #                     if key not in needed_ds_diem:
    #                         i.pop(key,None)
    #     stt+=1
    jsonKeyDeletor(data, needed_data)

    return data