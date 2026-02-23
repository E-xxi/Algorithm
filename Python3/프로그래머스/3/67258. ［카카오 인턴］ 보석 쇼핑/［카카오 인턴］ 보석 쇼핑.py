#진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간
#가장 짧은 구간이 여러 개라면 시작 진열대 번호가 가장 작은 구간
from collections import Counter
#종류니까 set, 범위니까 투포인터
def solution(gems):
    answer = [0,0]
    gcnt= len(set(gems))
    start, end = 0,gcnt
    l = float('inf')
    
    gem_dict = dict(Counter(gems[start:end-1]))
    
    for end in range(gcnt-1, len(gems)):   
        if gems[end] not in gem_dict:
            gem_dict[gems[end]] = 0
        gem_dict[gems[end]] += 1  
        
        while len(gem_dict) == gcnt:   
            if (end - start) < l:
                answer[0] = start+1
                answer[1] = end+1
                l = end - start
                
            g = gems[start]
            gem_dict[g] -= 1
            if gem_dict[g] == 0:
                del gem_dict[g]
            start +=1
    
    return answer
