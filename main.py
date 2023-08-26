import requests
import json
from API import *
from Module import *

with requests.Session() as sess:
    login_data = {
        'username': 'N21DCCN165',
        'password': '25092003',
        'grant_type': 'password'
    }
    Login(sess, login_data)

    user_info = Info(sess)
    user_score = Score(sess)
    user_schedule = TimeTable(sess, 20231)
    user_fee = Fee(sess)
    user_test_shedule = ExamSchedule(sess, 20221)

    with open('user_info.json', 'w', encoding='utf-8') as f:
        json.dump(user_info, f, ensure_ascii=False, indent=4)

    with open('user_score.json', 'w', encoding='utf-8') as f:
        json.dump(user_score, f, ensure_ascii=False, indent=4)

    with open('user_schedule.json', 'w', encoding='utf-8') as f:
        json.dump(user_schedule, f, ensure_ascii=False, indent=4)
    
    with open('user_fee.json', 'w', encoding='utf-8') as f:
        json.dump(user_fee, f, ensure_ascii=False, indent=4)

    with open('user_test_schedule.json', 'w', encoding='utf-8') as f:
        json.dump(user_test_shedule, f, ensure_ascii=False, indent=4)
