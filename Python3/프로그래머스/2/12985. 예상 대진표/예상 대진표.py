import math 
def solution(n,a,b):
    answer = 0
    
    #1,2, 3,4, 5,6, 7,8
    #1    2    3    4
    for i in range(n//2+1):
        #확인 향후의 인덱스 값끼리 비교하면됨
        a, b = math.ceil(a/2), math.ceil(b/2)
        answer += 1
        if a == b:
            return answer        
        
    return answer

