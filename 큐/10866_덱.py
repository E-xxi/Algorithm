#deque는 앞뒤에 다 넣고 빼고 할수있는 신기한 친구임!! 큐 + 스택
#파이썬에는 deque가 이미 존재함
from collections import deque
# stack과 거의 비슷하고 appendleft 이런 식으로 사용하면 됨
import sys
input = sys.stdin.readline

n = int(input())
deq = deque()

a=0; b=0

if a == b:
    print('equal')

for _ in range(n):
    menu = input().split()
    if menu[0] == 'push_front':
        deq.appendleft(menu[1])
    elif menu[0] == 'push_back':
        deq.append(menu[1])
    elif menu[0] == 'pop_front':
        if len(deq) == 0:   print(-1)
        else:   print(deq.popleft())
    elif menu[0] == 'pop_back':
        if len(deq) == 0:   print(-1)
        else:   print(deq.pop())
    elif menu[0] == 'size':
        print(len(deq))
    elif menu[0] == 'empty':
        if len(deq) == 0:   print(1)
        else:   print(0)
    elif menu[0] == 'front':
        if len(deq) == 0:   print(-1)
        else:   print(deq[0])
    else:
        if len(deq) == 0:   print(-1)
        else:   print(deq[len(deq)-1])

