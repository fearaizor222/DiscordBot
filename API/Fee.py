import requests
from Module import jsonKeyDeletor
from global_configuration import *

def requestFee(sess: requests.Session) -> dict:
    data = sess.post(ENDPOINT['Xem_Hoc_Phi'], timeout=CONFIG['timeout']).json()['data'].pop('ds_hoc_phi_hoc_ky')
    needed_data = ['ten_hoc_ky', 'hoc_phi', 'da_thu', 'con_no', 'mien_giam', 'phai_thu', 'tong_hoc_bong']

    jsonKeyDeletor(needed_data)

    return data