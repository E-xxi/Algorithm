def solution(s):
    answer = 0    
    # 애초에 시작 문자열이 불완전한 경우 처리
    if len(s) % 2:
        return 0
    
    dic = {')':'(',']':'[','}':'{'}
    s2 = s*2 #뒤에 하나 더 붙여서 회전
    
    for i in range(0,len(s)):
        ns = s2[i:i+len(s)] #새로운 문자열
        stack = []
        #print(ns)
        for c in ns:
            if c in dic.values():
                stack.append(c)
            else: #stack의 가장 마지막 괄호와 닫는 가장 첫 괄호가 같은 종류여야함.
                if (dic[c] not in stack) or (not stack) or(stack[-1] != dic[c]):
                    break
                stack.pop()
                    
        else:
            if not stack:
                answer += 1
                #print('0')
    return answer