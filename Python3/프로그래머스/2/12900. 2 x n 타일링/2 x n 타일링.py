def solution(n):
    #n=1 일때 1가지 방법
    #n=2, 2
    #n=3, 3
    #n=4, 5
    
    a,b = 0,1
    for _ in range(1,n+1):
        a,b = b, a+b
    
    return b %1000000007
