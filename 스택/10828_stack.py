import sys
stack = []
N = int(input())  # 데이터 개수 입력

for _ in range(N):
    com = sys.stdin.readline().split()
    if com[0] == "push":
        num = int(com[1])
        stack.append(num)
    elif com[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif com[0] == "size":
        print(len(stack))
    elif com[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:  # top
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
