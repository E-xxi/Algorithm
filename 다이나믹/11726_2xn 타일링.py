import sys
input = sys.stdin.readline

n = int(input().rstrip())
tile = [0 for _ in range(n)]

tile[0] = 1
tile[1] = 2
t

for i in range(2,n):
    tile[i] = (tile[i-1] + tile[i-2]) % 10007

print(tile[n-1]) # 세로짜리만 쓰는 경우 더해주기

