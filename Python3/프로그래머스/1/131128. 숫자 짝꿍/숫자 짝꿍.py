from collections import Counter

def commonalpha(X,Y):    # 공통 알파벳만 추출
    common = []
    l = Counter(list(set(X)) + list(set(Y))).items()

    for k, v in l:
        if v == 2:
            common.append(k)
        
    return sorted(common)

def solution(X, Y):
    both = commonalpha(X,Y)
    answer = []
    
    #print(f'both {both}')
    if not both:
        return '-1'
    
    if (len(both) == 1) and (both[0] == '0'):
        return '0'
    
    #각각 양쪽에 몇개있는지 알아야함
    for b in both:
        answer = answer + [b] * min(X.count(b), Y.count(b))
        #print(a, count, new)
    
    return ''.join(sorted(answer,reverse = True))