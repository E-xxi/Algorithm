def solution(n, lost, reserve):
    answer = 0
    a = [s for s in range(1,n+1)]
    
    new_lost = []
    for l in lost:
        if l in reserve:
            reserve.remove(l)
        else:
            new_lost.append(l)
    
    for i in a:
        if i in new_lost  : #가져온것도 없고 잃어버린 경우
            if i-1 in reserve:
                reserve.remove(i-1)
                answer+=1
            elif i+1 in reserve:
                reserve.remove(i+1)
                answer+=1
        else:
            answer+=1
    
    return answer