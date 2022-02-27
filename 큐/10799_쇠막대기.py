#레이저와 쇠막대가 각 몇개인지 먼저 알아보자
import sys
input=sys.stdin.readline
block = input().rstrip()

stack = 0
total = 0   #전체 막대기 수
i=0
while i != len(block)-1:
    if block[i] == '(':
        if block[i+1] == ')': #() 이렇게 닫혀서 레이저인 경우
            total += stack
            i+=1
        else:   #쇠막대인경우
            total += 1
            stack += 1
    else:   # )로 막대기가 끝난다면
        stack -= 1
    i+=1
print(total)




