import sys
input = sys.stdin.readline

line = list(input().rstrip())
dic=[]
for i in range(len(line)):
    dic.append(line[i:])
dic.sort()

for word in dic:
    print(''.join(word))
