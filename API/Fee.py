import json
import requests
import Module.JsonKeyDeletor as JsonKeyDeletor
from global_config import *

def Fee(sess: requests.Session) -> dict:
    data = sess.post(API_Endpoint['Xem_Hoc_Phi'], timeout=config['timeout']).json()['data'].pop('ds_hoc_phi_hoc_ky')
    needed_data = ['ten_hoc_ky', 'hoc_phi', 'da_thu', 'con_no', 'mien_giam', 'phai_thu', 'tong_hoc_bong']

    JsonKeyDeletor(data, needed_data)

    return data