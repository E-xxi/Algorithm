def cal_date(today, term): #모든 달은 28일까지
    year,month,day = (map(int,today.split('.')))
    
    month += term
    day -= 1
    if day == 0:
        day = 28
        month -=1
        
    if month > 12:
        year += (month-1) // 12
        
    return f'{year}.{str((month-1)%12+1).zfill(2)}.{str(day).zfill(2)}'

def solution(today, terms, privacies):
    answer = []
    terms = dict([t.split() for t in terms])

    for idx, row in enumerate(privacies):
        date, t = row.split()
        dueday = cal_date(date, int(terms[t]))
        
        if today > dueday:
            answer.append(idx+1)
    return answer 