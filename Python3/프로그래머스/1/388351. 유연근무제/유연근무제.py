def cal_standard_time(standard):
    # 시간범위 재설정
    # 958 + 10 -> 1008이어야됨. 
    hour = standard // 100
    minute = standard % 100
    if minute >= 50:
        hour += 1
        minute -= 60
    return hour*100 + minute +10


def solution(schedules, timelogs, startday):
    answer = 0
    
    for standard, person in zip(schedules, timelogs):
        late = False
        for i, checked in zip(range(0,7), person):
            day = ( startday + i ) % 7
            print(day, standard, i, checked)
            
            if (day == 6) or (day == 0): # 주말
                continue
            
            if cal_standard_time(standard)< checked: #지각하면
                late = True
                break
            
        if late == False:
            answer+=1
            
    return answer