from itertools import combinations
import math
def solution(nums):
    answer = 0
    
    comb = [sum(n) for n in list(combinations(nums, 3))]
    print(comb)
    for num in comb: #comb의 최소값은 6부터
        for i in range(2,int(num ** (1/2))+1):
            if num % i == 0:
                #print(num,i)
                break
        else:
            answer += 1
                
    return answer