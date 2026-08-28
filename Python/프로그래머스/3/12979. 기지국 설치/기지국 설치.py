import math
def solution(n, stations, w):
    answer = 0
    cover = 2*w + 1
    prev_end = 0  #마지막지점
    
    for s in stations:
        left = s - w # 커버 첫 지점
        gap = left - prev_end - 1
        
        if gap > 0:
            answer += math.ceil(gap / cover)
        
        prev_end = s + w
    
    # 마지막 기지국 이후 빈 구간
    if prev_end < n:
        gap = n - prev_end
        answer += math.ceil(gap / cover)
    
    return answer
