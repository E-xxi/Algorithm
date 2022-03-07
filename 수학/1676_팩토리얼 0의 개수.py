n = int(input())
r = 1
while n > 1:
    r *= n
    n -= 1
rlist = list(map(int, str(r)))
c=0
for e in rlist[-1:0:-1]:
    if e != 0:
        break
    c += 1
print(c)