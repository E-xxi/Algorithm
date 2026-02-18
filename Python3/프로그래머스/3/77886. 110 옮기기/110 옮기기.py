from collections import deque

def cnt110(n):
    stack = []
    cnt = 0
    
    for c in n:
        stack.append(c)
        if stack[-3:] == ['1','1','0']:
            stack.pop()
            stack.pop()
            stack.pop()
            cnt += 1
            
    return ''.join(stack), '110'*cnt

def solution(s):
    answer = []
    
    for n in s:
        n,insert = cnt110(list(n))
        
        idx = n.rfind('0')
        answer.append(n[:idx+1]+insert+n[idx+1:])

    return answer