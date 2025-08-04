def solution(survey, choices):
    answer = ''
    pers = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    score = {1:3,2:2,3:1, 4:0, 5:1,6:2,7:3}
    
    for s, c in zip(survey, choices):
        #print(s, c)
        if c > 4: # 4이상이면 뒤에껄로
            pers[s[1]] += score[c]
        else:
            pers[s[0]] += score[c]       
    
    #print(pers)
    answer += 'R' if pers['R'] >= pers['T'] else 'T'
    answer += 'C' if pers['C'] >= pers['F'] else 'F'
    answer += 'J' if pers['J'] >= pers['M'] else 'M'
    answer += 'A' if pers['A'] >= pers['N'] else 'N'
    return answer
