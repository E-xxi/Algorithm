N, M, K = map(int, list(input().split()))

team = 0 
while True:
    N -= 2
    M -= 1 # 이렇게 하면 1팀 완성
    
    # 종료조건
    if (N < 0) or (M < 0) or (N+M < K):
        break
    team += 1

print(team)