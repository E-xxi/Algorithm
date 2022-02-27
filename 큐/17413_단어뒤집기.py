import sys

input = sys.stdin.readline
lines = list(input())

stack = list()

i = 0
while i != len(lines) - 1:
    if '<' == lines[i]:  # > 전까지 저장
        while True:
            print(lines[i], end='')
            if lines[i] == '>':
                break
            i += 1
    elif ' ' == lines[i]:
        print(' ', end='')
    else:
        stack.append(lines[i])
        if ' ' == lines[i + 1] or '<' == lines[i + 1] or '\n' == lines[i + 1]:
            # pop시키면서 출력
            while len(stack) != 0:
                print(stack.pop(), end='')
    i += 1