def polynominal(str):
    p = 31
    m = 100001
    
    v = 0 
    for s in str:
        v = (v* p + ord(s)) % m
    return v

from collections import Counter
def solution(participant, completion):
    completion = Counter(completion)
    
    for p in participant:
        if p not in completion.keys():
            return p
        completion[p] -= 1
        if completion[p] == 0:
            completion.pop(p)
        
        
            
    
        