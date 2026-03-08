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
    return -1 if min(dp) == float('inf') else min(dp)