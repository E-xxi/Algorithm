from collections import deque
#B팀이 얻는 최대 승점(숫자가 큰 쪽이 승리) -하나만 틀린코드
def solution(A, B):
    answer = 0
    
    A = deque(sorted(A))
    B = deque(sorted(B, reverse = True))
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
