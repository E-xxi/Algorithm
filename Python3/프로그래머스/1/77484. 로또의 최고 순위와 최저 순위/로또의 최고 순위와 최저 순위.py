from collections import Counter
def solution(lottos, win_nums):
    answer = [0,0]
    zero = lottos.count(0)
    
    match = 0
    for n,cnt in Counter(lottos+win_nums).items():
        if cnt == 2 and n != 0:
            match +=1

    return [min(7-(match+zero),6), min(7-match, 6)]
# 23456
#654321