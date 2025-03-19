def solution(a, d, included):
    answer = 0
    
    #exp = dx+a
    for i in range(len(included)):
        if included[i]:
            answer += d*i+a
            
    return answer