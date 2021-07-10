
from datetime import datetime, timedelta, time
from .models import RestRequest,Schedule
from datetime import datetime, timedelta, time, date
from django.db.models import Q
import json


#送られてきたシフトを登録する
def submit_rest_requests(input_data:dict):
    #new_rest_request = RestRequest.objects.create()

    #make_schedules(input_data)
    return input_data

#DBから該当の日付を持ってきて出力する
def get_scheduls(input_data:dict):

    val = ""
    return val


def make_schedules(input_data:dict):
    val = ""
    return val