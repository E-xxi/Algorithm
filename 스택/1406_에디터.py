# 한줄 에디터 영어 소문자만 최대 600000글자
import sys
input = sys.stdin.readline

stack = list(input().rstrip())
m = int(input())
rest = []

for _ in range(m):
    com = input().split()
    if com[0] == 'L':  # 커서를 왼쪽으로 하나 옮김
        if  len(stack) != 0:
            rest.append(stack.pop())
    elif com[0] == 'D':    #커서를 오른쪽 한칸
        if len(rest) != 0:
            stack.append(rest.pop())
    elif com[0] == 'B':    # 삭제
        if len(stack) != 0:
            stack.pop()
    else:   #추가
        stack.append(com[1])

for element in stack + list(reversed(rest)):
    print(element, end='')









