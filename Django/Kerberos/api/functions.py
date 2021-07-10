
from datetime import datetime, timedelta, time
from .models import RestRequest,Schedule
from datetime import datetime, timedelta, time, date
from django.db.models import Q
import json


#送られてきたシフトを登録する
def submit_rest_requests(input_data:dict):
    kerbero_id = input_data["kerbero_id"]
    head_name = input_data["head_name"]

    rest_requests = RestRequest.objects.filter(kerbero_id=kerbero_id,head_name=head_name,date__gte=date.today())

    for req in input_data["request"]:
        req_date = datetime.strptime(req["date"],'%Y-%m-%d').date()
        requested = False

        flag = 0
        for checked_val in rest_requests:
            if checked_val.date == req_date:
                flag = 1
                break
        if flag:
            continue

        if req["request"]:
            requested = True
            start_time = datetime.strptime(req["start_time"],"%H:%M").time()
            end_datetime = make_end_datetime(req_date,req["end_time"])
            RestRequest.objects.create(kerbero_id=kerbero_id,head_name=head_name,requested=requested,date=req_date,start_time=start_time,end_datetime=end_datetime)
        else:
            RestRequest.objects.create(kerbero_id=kerbero_id,head_name=head_name,requested=requested,date=req_date)

        make_schedules(rest_requests,input_data)
        
    return input_data

#DBから該当の日付を持ってきて出力する
def get_scheduls(input_data:dict):

    val = ""
    return val


def make_schedules(rest_requests,input_data:dict):
    val = ""
    return val




def make_end_datetime(req_date,end_time:str):
    return_date = req_date
    end_time_hour = int(end_time[:end_time.find(':')])  # スライスで半角空白文字よりも前を抽出
    if end_time[(end_time.find(':')+1):]=="00" or end_time[(end_time.find(':')+1):]=="0":
        end_time_minute = 0
    else:
        end_time_minute = int(end_time[(end_time.find(':')+1):])

    print(return_date)
    print(end_time_hour)
    if end_time_hour >= 24:
        return_date = date(req_date.year,req_date.month,req_date.day+1)
        end_time_hour -= 24
        
    return datetime(return_date.year,return_date.month,return_date.day,end_time_hour,end_time_minute)