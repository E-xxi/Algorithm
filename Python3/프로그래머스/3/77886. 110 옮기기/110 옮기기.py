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
        #left- 110빼고 남은 숫자열 / insert - '110'*개수
        left,insert = cnt110(list(n)) 
        #print(left,insert)
        
        #다시 삽입했을때 사전순으로 가장 앞에 있는거 
        idx = left.rfind('0')
        #print(idx)
        answer.append(left[:idx+1]+insert+left[idx+1:])

    return answer