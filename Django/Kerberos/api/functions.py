
from datetime import datetime, timedelta, time
from .models import RestRequest,Schedule
from datetime import datetime, timedelta, time, date
from django.db.models import Q
import json


#送られてきたシフトを登録する
def submit_rest_requests(input_data:dict):
    kerbero_id = input_data['kerbero']
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
            new_rest_request = RestRequest.objects.create(kerbero_id=kerbero_id,head_name=head_name,requested=requested,date=req_date,start_time=start_time,end_datetime=end_datetime)
        else:
            new_rest_request = RestRequest.objects.create(kerbero_id=kerbero_id,head_name=head_name,requested=requested,date=req_date)

        make_schedules(new_rest_request)
        
    return input_data

#DBから該当の日付を持ってきて出力する
def get_schedules(input_data:dict):
    appear_date = datetime.strptime(input_data["start_date"],'%Y-%m-%d').date()
    end_date = appear_date + timedelta(days=7)
    kerbero_id = input_data["kerbero_id"]

    val = {"schedules":[]}

    for v in  Schedule.objects.filter(kerbero_id = kerbero_id,date__range=[appear_date,end_date]):
        val["schedules"].append({"date":v.date.strftime('%Y-%m-%d'),"shift":[{"head_name":"left","start_time":v.left_start_time,"end_time":v.left_end_time},{"head_name":"center","start_time":v.center_start_time,"end_time":v.center_end_time},{"head_name":"right","start_time":v.right_start_time,"end_time":v.right_end_time}]})
    
    return val



def make_schedules(new_rest_request:RestRequest):
    rest_requests = RestRequest.objects.filter(kerbero_id=new_rest_request.kerbero_id,date=new_rest_request.date)
    date_of = new_rest_request.date
    name_set = []
    print(rest_requests)

    for val in rest_requests:
        name_set.append(val.head_name)

    print(name_set)

    setting_val = []
    
    if ("left" in name_set) and ("center" in name_set) and ("right" in name_set):

        for i, val in enumerate(rest_requests):
            current_head = val.head_name
            print(val.start_time)
            current_start_datetime = datetime(val.date.year, val.date.month, val.date.day, val.start_time.hour, val.start_time.minute)
            current_end_datetime = val.end_datetime
            
            if i == 0:
                setting_val.append({"head_name":current_head,"start_time":current_start_datetime,"end_time":current_start_datetime+timedelta(hours=6)})

            elif i == 1:
                #希望開始時刻が先に入力した人の睡眠シフト内だった場合は、後ろにずらせるなら後ろにずらす
                if current_start_datetime >= setting_val[0]["start_time"] and current_start_datetime <= setting_val[0]["end_time"]:
                    if setting_val[0]["end_time"].hour >= 6:
                        setting_val.append({"head_name":current_head,"start_time":setting_val[0]["end_time"],"end_time":setting_val[0]["end_time"]+timedelta(hours=6)})

                    else:
                        setting_val.append({"head_name":current_head,"start_time":setting_val[0]["start_time"]-timedelta(hours=6),"end_time":setting_val[0]["start_time"]})
                
                elif current_end_datetime >= setting_val[0]["start_time"] and current_end_datetime <= setting_val[0]["end_time"]:
                    if setting_val[0]["start_time"].hour >= 6:
                        setting_val.append({"head_name":current_head,"start_time":setting_val[0]["start_time"]-timedelta(hours=6),"end_time":setting_val[0]["start_time"]})

                    else:
                        setting_val.append({"head_name":current_head,"start_time":setting_val[0]["end_time"],"end_time":setting_val[0]["end_time"]+timedelta(hours=6)})

                else:
                    setting_val.append({"head_name":current_head,"start_time":current_start_datetime,"end_time":current_start_datetime+timedelta(hours=6)})

            elif i == 2:
                if (current_start_datetime <= (setting_val[0]["start_time"] - timedelta(hours=6)) and current_start_datetime <= (setting_val[1]["start_time"] - timedelta(hours=6))) or (current_start_datetime <= (setting_val[0]["start_time"] - timedelta(hours=6)) and current_start_datetime >= (setting_val[1]["end_time"])) or (current_start_datetime <= (setting_val[1]["start_time"] - timedelta(hours=6)) and current_start_datetime >= (setting_val[0]["end_time"])) or (current_start_datetime >= (setting_val[0]["end_time"]) and current_start_datetime <= (setting_val[1]["end_time"])):
                    setting_val.append({"head_name":current_head,"start_time":current_start_datetime,"end_time":current_start_datetime+timedelta(hours=6)})

                elif (current_end_datetime <= (setting_val[0]["start_time"]) and current_end_datetime <= (setting_val[1]["start_time"])) or (current_end_datetime <= (setting_val[0]["start_time"]) and current_end_datetime >= (setting_val[1]["end_time"] + timedelta(hours=6))) or (current_end_datetime <= (setting_val[1]["start_time"]) and current_end_datetime >= (setting_val[0]["end_time"] + timedelta(hours=6))) or (current_end_datetime >= (setting_val[0]["end_time"] + timedelta(hours=6)) and current_start_datetime <= (setting_val[1]["end_time"] + timedelta(hours=6))):
                    setting_val.append({"head_name":current_head,"start_time":current_end_datetime-timedelta(hours=6),"end_time":current_end_datetime})

                elif ((setting_val[0]["start_time"].hour >= 6) and (setting_val[1]["start_time"].hour >= 6)):
                    current_check_val = setting_val[0]["start_time"]
                    if current_check_val > setting_val[1]["start_time"]:
                        current_check_val = setting_val[1]["start_time"]

                    setting_val.append({"head_name":current_head,"start_time":current_check_val-timedelta(hours=6),"end_time":current_check_val})

                else:
                    current_check_val = setting_val[0]["end_time"]
                    if current_check_val < setting_val[1]["end_time"]:
                        current_check_val = setting_val[1]["end_time"]

                    setting_val.append({"head_name":current_head,"start_time":current_check_val,"end_time":current_check_val + timedelta(hours=6)})
                    
        left_val = {}
        center_val = {}
        right_val = {}
        for val in setting_val:
            if val["head_name"] == "left":
                left_val["start_time"] = val["start_time"].strftime('%H:%M')
                left_val["end_time"] = make_end_time_str(val["start_time"],val["end_time"])

            elif val["head_name"] == "center":
                center_val["start_time"] = val["start_time"].strftime('%H:%M')
                center_val["end_time"] = make_end_time_str(val["start_time"],val["end_time"])
            
            elif val["head_name"] == "right":
                right_val["start_time"] = val["start_time"].strftime('%H:%M')
                right_val["end_time"] = make_end_time_str(val["start_time"],val["end_time"])

        Schedule.objects.create(kerbero_id=new_rest_request.kerbero_id,date=date_of,left_start_time = left_val["start_time"],left_end_time = left_val["end_time"],center_start_time = center_val["start_time"],center_end_time = center_val["end_time"],right_start_time = right_val["start_time"],right_end_time = right_val["end_time"])


    else:
        pass




#2021-7-12:date,"30:00":strみたいなやつを受け取ったら、2021-7-12 6:00:datetimeを返す。日を跨いでなかったらそのままdatetimeに変形だけして返す
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


def make_end_time_str(start_time,end_time):
    print(end_time.date())
    if start_time.date() == end_time.date():
        return end_time.strftime('%H:%M')

    else:
        return str(end_time.hour + 24) + ":" + plus_zero(str(end_time.minute))


def plus_zero(str_min:str):
    if str_min == "0":
        str_min = "00"
    return str_min