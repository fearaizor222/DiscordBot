import requests
import json
from API import *
from Module import *

with requests.Session() as sess:
    login_data = {
        'username': 'n21dccn165',
        'password': '25092003',
        'grant_type': 'password'
    }
    Login(sess, login_data)


