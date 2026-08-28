from collections import deque
def solution(people, limit): #최대 2명 #최대한 적게 구명보트
    answer = 0
    
    people = deque(sorted(people))
    
    while people:
        if (len(people) > 1) and (limit -people[0] -people[-1] >= 0):
            people.popleft()
        people.pop()
            
        answer += 1
    return answer