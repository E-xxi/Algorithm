import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
T = Counter(A)
print(T)
result = [-1] * n
stack = [0]

#여기 위치 삽입하는게 반드시 index로 stack에 넣어야지만 결과가 나옴
for i in range(1, n):
    while stack and T[A[stack[-1]]] < T[A[i]]:
        result[stack.pop()] = A[i]
    stack.append(i)

print(*result)
