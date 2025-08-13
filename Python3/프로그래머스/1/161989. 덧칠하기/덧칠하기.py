from collections import deque
def solution(n, m, section): #section은 다시 칠해야되는 번호
    answer = 0
    #n: 전체 길이
    #m: 롤러길이
    
    section = deque(section)
    while section:
        p = section.popleft()
        answer+=1
        
        while section:
            if section[0] < p+m:
                section.popleft()
            else:
                break
        
            
            
        
    
            
    
    
    return answer