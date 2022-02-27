import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
result = [-1] * N
stack = [0]

#여기 위치 삽입하는게 반드시 index로 stack에 넣어야지만 결과가 나옴
for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        result[stack.pop()] = A[i]
    stack.append(i)

print(*result)