from collections import deque
#B팀이 얻는 최대 승점(숫자가 큰 쪽이 승리) -하나만 틀린코드
def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    
    if B[0] <= A[0]: # B의 최대값이 A의 최소값보다 작으면 
        return 0
    
    A = deque(A)
    B = deque(B)
    #질때는 가장 작은거를 내고 져야되고
    #이길때는 가장 비슷한걸 내고 이겨야함. 
    while A:
        a = A.pop()
        if B[0] > a: # B제일 큰 값으로 이길수있다.
            answer += 1
            B.popleft()
        else:#지거나 비기면 작은걸 내도록?
            B.pop()
            
    return answer
'''from collections import deque
#B팀이 얻는 최대 승점(숫자가 큰 쪽이 승리) -하나만 틀린코드
def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    
    if B[0] <= A[0]: # B의 최대값이 A의 최소값보다 작으면 
        return 0
    
    A = deque(A)
    B = deque(B)
    #질때는 가장 작은거를 내고 져야되고
    #이길때는 가장 비슷한걸 내고 이겨야함. 
    while A:
        a = A.pop()
        if B[0] > a: # B제일 큰 값으로 이길수있다.
            answer += 1
            B.popleft()
        elif B[0] == a: #비긴다도 생각해야되나
            B.popleft()
        else:#지면
            B.pop()
            
    return answer'''