#요세푸스 순열을 구하는 문제
#원형 큐를 이용해보자
import sys
input = sys.stdin.readline

n, k = map(int,(input().split()))
#인덱스가 k의 배수가 되는 숫자를 차례로 삭제!
que = list()   #원형 큐를 위한 틀
que.extend(range(1,n+1))
result = []
f = 1

while(len(que) != 0):   #que가 비면 끝나는것
    l = len(que)
    c = 0
    for i in range(0,l):
        if f % k == 0:
            result.append(str(que.pop(i+c)))
            c -= 1
        f+=1  # 하나씩 밀면서

print('<'+', '.join(result)+'>')