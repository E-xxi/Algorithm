import sys

input = sys.stdin.readline

n = int(input())

queue = []
for _ in range(n):
    order = input().split()
    if order[0] == 'push':
        queue.append(order[1])
    elif order[0] == 'pop':
        if len(queue) != 0:
            print(queue.pop(0))
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    else:
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)