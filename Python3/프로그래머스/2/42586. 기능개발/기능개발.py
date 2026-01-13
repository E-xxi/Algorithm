from collections import deque
import numpy as np

def solution(progresses, speeds):
    left = deque([100-p for p in progresses])
    speeds = deque(speeds)
    answer = []
    # 제일 앞에꺼가 완료되는 날짜에 같이 완료될수 있는거 아웃.
    
    while left:
        day = left[0] // speeds[0] + bool(left[0]%speeds[0])
        left.popleft()
        speeds.popleft()
        
        for i in range(len(left)):
            left[i] -= speeds[i]*day
        
        cnt = 1
        while left:
            if left[0] <= 0:
                cnt += 1 
                left.popleft()
                speeds.popleft()
            else:
                break
        
        answer.append(cnt)        
    return answer