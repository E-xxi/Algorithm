def solution(d, budget):
    answer = 0
     #최대 많은 부서
        
    d.sort(reverse = True)
    
    while d:
        m = d.pop()
        if budget - m >= 0:
            #print(m, budget)
            budget -= m
            answer+=1
        else:
            return answer
    

    return answer