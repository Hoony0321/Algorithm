import math
def solution(fees, records):
    answer = []
    min_time, min_fee, unit_time, unit_fee = fees
    park_dict = dict()
    
    
    for record in records:
        time, car_number, is_enter = record.split(" ")
        
        if car_number not in park_dict:
            park_dict[car_number] = [time]
        else:
            park_dict[car_number].append(time)
            
    for car_number in sorted(list(park_dict.keys())):
        record = park_dict[car_number]
        
        def cal_time_diff(time1, time2):
            hour1,min1 = map(int,time1.split(":"))
            hour2,min2 = map(int,time2.split(":"))
            
            return (hour2*60 + min2) - (hour1*60 + min1)
        
        def cal_park_fee(time):
            if time <= min_time:
                return min_fee
            else:
                return min_fee + unit_fee * math.ceil((time - min_time)/unit_time)
        
        sum_park_time = 0
        while(len(record) > 0):
            if(len(record) == 1):
                sum_park_time += cal_time_diff(record[0],"23:59")
                record = []
            else:
                sum_park_time += cal_time_diff(record[0],record[1])
                del record[:2]
                
        answer.append(cal_park_fee(sum_park_time))
    
    return answer