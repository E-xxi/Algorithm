def convert(n, k):
    if n<k:
        return str(n)
    return convert(n//k,k) + str(n%k)
    
    
def solution(n, k):
    answer = 0
    
    for cn in convert(n,k).split('0'):
        if cn and cn > '1':
            cn = int(cn)
            for i in range(2, int(cn**(1/2))+1):
                if cn % i == 0:
                    break
            else:
                answer += 1
    
    return answer