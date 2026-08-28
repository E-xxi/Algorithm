
def solution(a):
    answer = set()
    n = len(a)
    # 더 작은걸 터트리는건 한번만 할 수 있음
    #키는 i-1, i+1 양쪽보다 작은 값이면 무조건 사라짐
    # 더 큰걸 터트리는거로 선택해도 어차피 더 작은 값이니
    #왼쪽에서 오른쪽으로 보면서 현재까지의 최솟값인지 확인
    min_a = float('inf')
    for i in range(n):
        if a[i] < min_a:
            #print(a[i])
            min_a = a[i]
            answer.add(min_a)
    
    min_a = float('inf')
    for i in range(n-1,0,-1):
        if a[i] < min_a:
            #print(a[i])
            min_a = a[i]
            answer.add(min_a)
        
        
    return len(answer)