from collections import Counter
def solution(topping):
    answer = 0
    #공평하게 자르는 방법수
    #토핑의 각각 len(set)값이 동일해야됨
    
    tops = dict(Counter(topping))
    rest = dict()
    
    for t in topping:
        if t not in rest:
            rest[t] = 0
        rest[t] += 1
        tops[t] -= 1
        if tops[t] == 0:
            tops.pop(t)
        if len(rest) == len(tops):
            answer += 1
    
    
    return answer