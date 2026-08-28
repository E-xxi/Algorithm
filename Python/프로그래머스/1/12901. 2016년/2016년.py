def solution(a, b):
    answer = ''
    week_dic = {0:'FRI',1:'SAT',2:'SUN',3:'MON',4:'TUE',5:'WED',6:'THU'}
    month_dic=[31,29,31,30,31,30,31,31,30,31,30,31]
    
    #윤년은 29일
    day = sum(month_dic[:a-1])-1
    day += b
    print(day)
    return week_dic[day%7]