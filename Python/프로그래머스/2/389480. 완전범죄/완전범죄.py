from collections import deque
def solution(info, n, m):
    answer = float('inf')
    
    l = len(info)
    que = deque([])
    if info[0][0] < n:
        que.append([0,info[0][0],0])
    if info[0][1] < m:
        que.append([0,0,info[0][1]])
    
    visited = set()
    
    while que:        
        idx, cn, cm = que.popleft()
        
        if (idx, cn, cm) in visited:
            continue
        visited.add((idx, cn, cm))
        
        if idx+1 >= l:
            answer = min(cn,answer)
            #print(idx,cn,cm)
            continue
        
        newa, newb = info[idx+1]
        if (cn+newa < n) and (cm < m):
            que.append([idx+1, cn+newa, cm])
        if (cn < n) and (cm+newb < m):
            que.append([idx+1, cn, cm+newb])
    
    return -1 if answer == float('inf') else answer
        
'''
def solution(info, n, m):
    answer = 0
    
    #B흔적이 b까지 왔을때 a의 가능한 최소 흔적?
    # b가 x 지점에서 a = dp[x]
    dp= [float('inf')]*m
    dp[0] =0
    
    for a,b in info:
        temp = [float('inf')]*m
        
        for x in range(m):
            if dp[x] == float('inf'):
                continue
            
            if dp[x] + a < n: #가 가능
                temp[x] = min(temp[x], dp[x] + a)  
            
            if x + b < m: #b가 가능
                temp[x+b] = min(temp[x+b], dp[x])   
    
        dp = temp
    
    print(min(dp))
    return -1 if min(dp) == float('inf') else min(dp)'''