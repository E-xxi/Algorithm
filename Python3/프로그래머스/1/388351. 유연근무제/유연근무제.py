def solution(schedules, timelogs, startday):
    answer = 0
    #출근희망시각+10분까지 출근
    #startday %7 +1, 6,7은 주말
    
    for s, timelog in zip(schedules, timelogs):
        hour,minutes = s//100, s%100
        hour += (minutes+10) //60
        minutes = (minutes+10) % 60
        
        for i in range(7):
            day = ((startday+i-1)%7+1)
            
            if day not in [6,7] and (hour*100+minutes < timelog[i]):
                break
        else:
            answer +=1
            
                
            
    return answer