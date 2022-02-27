#최대공약수 최소공배수
import sys
input = sys.stdin.readline

def gcd(a,b):
    while b != 0:
        s = a % b
        a = b
        b = s
    return a
def lcm(a,b):
    return a * b / gcd(a, b)

T = int(input())
for _ in range(T):
    a, b = map(int,input().split())
    print(int(lcm(a,b)))