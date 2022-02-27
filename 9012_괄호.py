#괄호가 완벽하게 쌍을 이룬 괄호문자열 VPS 확인하기
import sys

T = int(sys.stdin.readline())  #test 케이스 입력
for _ in range(T):
    ps = sys.stdin.readline()
    pStack = 0

    if (len(ps)-1)%2 == 1:   #홀수라면 안됨
        print('NO')
        continue

    for p in range(len(ps)-1):
        if ps[p] == '(':
            pStack += 1
        else:   # ) 이거일때
            pStack -= 1

        if pStack < 0:
            break

    if pStack == 0:
        print('YES')
    else:
        print('NO')