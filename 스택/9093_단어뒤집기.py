#단어 뒤집기 문자열을 list화 해서 pop 시킴
import sys
testNum = int(sys.stdin.readline())

for _ in range(testNum):
    line = sys.stdin.readline().split()    #list로 저장
    for i in range(len(line)):
        li = list(line[i])
        for j in range(len(li)):
            print(li.pop(),end='')
        if i != len(line)-1:
            print(' ',end='')
    print()
