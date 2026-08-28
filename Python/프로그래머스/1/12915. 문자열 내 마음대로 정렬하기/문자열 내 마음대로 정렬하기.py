def solution(strings, n):
    answer = 0
    strings = list(map(list, strings))
    strings = sorted(strings, key = lambda x: (x[n],x))
    
    return [''.join(s) for s in strings]