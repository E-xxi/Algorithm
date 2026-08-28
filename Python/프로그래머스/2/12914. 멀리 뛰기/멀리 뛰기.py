from math import factorial
def solution(n):
    answer = 1
    nl = []
    
    #5c2
    #5c3
    for i in range(1,n//2+1):
        nl= [2]*i + [1]*(n-i*2)
        #print(nl,i,len(nl))
        answer+=factorial(len(nl)) // (factorial(i)*factorial(len(nl)-i))
        #print(factorial(len(nl)))

        #3*2*1
        #/1*2*1
    return answer % 1234567

