import json
import requests

def Fee(sess: requests.Session()) -> dict:
    with open('API_Endpoint.json', 'r') as API:
        API_Endpoint = json.load(API)

    data = sess.post(API_Endpoint['Xem_Hoc_Phi']).json()['data'].pop('ds_hoc_phi_hoc_ky')
    needed_data = ['ten_hoc_ky', 'hoc_phi', 'da_thu', 'con_no', 'mien_giam', 'phai_thu', 'tong_hoc_bong']
    for obj in data:
        for key in list(obj):
            if key not in needed_data:
                obj.pop(key, None)
    return data