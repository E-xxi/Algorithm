import sys

stack = [0,]    # 스택
result = ''     # 수열을 만드는데 필요한 +/- 결과
n = int(sys.stdin.readline())

start = 1
for _ in range(n):
    sNum = int(sys.stdin.readline())    # 숫자 입력
    # top == sNum이면
    if stack[-1] == sNum:
        stack.pop()
        result += '-'
        continue    # 다음걸로 넘어감
    elif stack[-1] > sNum:
        print('NO')
        sys.exit()

    # sequence 요소와 다르다면
    for i in range(start,sNum+1):   # 본인까지 스택에 넣음
        stack.append(i)
        result += '+'
    stack.pop()
    result += '-'
    start = sNum+1

for r in result:
    print(r)
