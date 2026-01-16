from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    # 2가지 이상 메뉴구성/ 최소 2명 이상 주문된 조합
    for n in course:
        temp = []
        for unit in orders:
            temp+=(combinations(sorted(unit),n))
            #-> sorted: combination 입장에선 같은거지만 나중에 counter할땐 다르게 인식. 
        if temp:
            #가장 많이 함께 주문한 단품메뉴 개수
            count_comb = dict(Counter(temp).items())
            maxcnt = max(count_comb.values())
            
            for combo, cnt in (count_comb.items()): 
                if (cnt == maxcnt) and (maxcnt > 1):
                    answer.append(''.join(combo))
    
    return sorted(answer)