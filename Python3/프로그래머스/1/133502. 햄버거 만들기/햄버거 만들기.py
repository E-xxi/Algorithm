from collections import deque
def solution(ingredient):
    answer = 0
    ingredient = deque(ingredient)
    stack = []
    
    while ingredient:
        stack.append(ingredient.popleft())
        if stack[-4:] == [1,2,3,1]:
            answer +=1
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            
    return answer