import sys
input = sys.stdin.readline

r = 1000000
plist = [True for _ in range(r)]

#에라토스테네스의 체
#0은 ture로 되어있음
for i in range(2,int(r**0.6)):
    if plist[i]==True:
        for j in range(i*2, r, i) :
            if plist[j] == True :
                plist[j] = False

while True:
    n = int(input().rstrip())
    if n == 0:  break
    for i in range(3, r):
        if plist[i] == True:
            if plist[n - i] == True:
                print("%d = %d + %d" % (n, i, n - i))
                break