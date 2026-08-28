def jump(n):
    #print(n)
    if n <= 1:
        return 1
    return jump(n//2) + n%2

def solution(n):
    return jump(n)