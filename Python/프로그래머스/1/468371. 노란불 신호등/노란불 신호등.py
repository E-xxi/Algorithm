import math
def solution(signals):
    answer = 0
    # 노란불은 구간이다!!! 길이가 있음
    #math.lcm(*sigsums)+1
    siglen = [sum(sig) for sig in signals]
    
    yellow = False
    for i in range(1, math.lcm(*siglen)+1):
        for si in range(len(signals)):
            if not(signals[si][0] < i % siglen[si] <= signals[si][0]+signals[si][1]):
                break
        else:
            return i
        
    return -1