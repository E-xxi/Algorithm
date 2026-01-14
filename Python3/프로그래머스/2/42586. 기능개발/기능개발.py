from collections import deque
import math

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []
    # 제일 앞에꺼가 완료되는 날짜에 같이 완료될수 있는거 아웃.
    
    while speeds:
        cnt = 1
        dayleft = math.ceil((100 - progresses.popleft()) / speeds.popleft())

        if not speeds:
            return answer + [cnt]
        
        i = 0
        for _ in range(len(progresses)):
            progresses[i] += dayleft*speeds[i]
            if (i == 0) and (progresses[i] >= 100):
                cnt+=1
                progresses.popleft()
                speeds.popleft()
            else:
                i +=1
        answer.append(cnt)
        #print(dayleft, progresses)
        
               
    return answer