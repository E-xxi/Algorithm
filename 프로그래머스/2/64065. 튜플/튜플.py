from collections import Counter
def solution(s):
    #s가 표현하고 있는 튜플
    comb_nums = dict(Counter(s.replace('{','').replace('}','').split(",")))
    
    return list(map(int, dict(sorted(comb_nums.items(), key = lambda x:-x[1])).keys()))