def time_cal(pri_hour, pri_min, cal_method, sec_hour, sec_min):
    result_hour = pri_hour + sec_hour
    if cal_method is plus:
        result_min = pri_min + sec_min
        if result_min >= 60:
            additional_hour = (result_min/60)-(result_min%60)
            result_hour = result_hour + additional_hour
            result_min = result_min - (60*additional_hour)
    if cal_method is minus:
        result_min = pri_min - sec_min
        if result_min < 0:
            if result_min < -60:
                additional_hour = (result_min/60)-(result_min%60)
                result_hour = result_hour - additional_hour
                result_min = 60-result_min
        else:
            result_hour = result_hour - 1
            result_min = 60 - abs(result_min)
    return f"{result_hour}:{result_min}"

print(187/60)