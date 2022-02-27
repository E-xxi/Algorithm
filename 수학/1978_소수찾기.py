import sys
input = sys.stdin.readline

def prime(a):
    if a == 1:
        return False
    for i in range(2,int(a**0.5)+1):
        if(a % i ==0):
            return False
    return True

a, b = map(int,input().split())

for d in range(a,b+1):
    if prime(d):
        print(d)
