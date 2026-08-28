def solution(n, tops):
    dp = [1] * (2 * n + 2)
    
    
    for i in range(2, 2 * n + 2):
        # 일반적으로 하는 2 n 타일링 
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
        
        # 사다리꼴 모양으로 끝나는 지점마다 tops가 있는지 확인. 
        if i % 2 == 0 and tops[i // 2 - 1]:
            #있으면 dp[n-2]지점 모든 배치  + 삼각형 한거만큼 더 생기는거니까
            dp[i] += dp[i - 1]

    return dp[-1]


'''def solution(n, tops):
    MOD = 10007
    # 삼각형을 추가했을때
    # 이전에 공유되는 부분이 채워져있는경우< 예시의 맨아래 줄 이 경우면 새로 추가했을때 ▼▲ 이 사다리꼴로 채울 수 없음 
    # 공유부분을 덮(3) 방법
    a = [0 for _ in range(n)]
    a[0] = 1
    # 안덮 방법 3개 ( 위아래(1), 안덮방향(2), 정삼각형으로만(4))
    b = [0 for _ in range(n)]
    b[0] = 3 if tops[0] else 2 # 뚜껑 없음 2가지
    
    for k in range(1,n):
        # 공유부분만 채우는 방식
        a[k] = a[k-1] + b[k-1]
        
        if tops[k]: # 위 삼각형 존재
            # 공유부분 없음
            b[k] = a[k-1]*2 + b[k-1]*3
            #a는 1,4 방식 + 3이 아닐때 1,2,4
        else:
            b[k] = a[k-1] + b[k-1]*2
            # 3일땐 4만 가능 + 3아닐때 2,4
        
        a[k] %= MOD
        b[k] %= MOD
    
    
    return (a[n-1] + b[n-1])%MOD'''