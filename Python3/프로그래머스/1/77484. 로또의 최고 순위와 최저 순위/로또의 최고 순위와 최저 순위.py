from collections import Counter
def solution(lottos, win_nums):
    #순서 상관없고 번호만 맞으면 됨.
    cero = Counter(lottos)[0] # 모르는 번호 개수
    
    cnt = 0
    for l in lottos:
        if l in win_nums:
            cnt += 1

    #최고 순위 / 최저순위
    return [min(6, 7 - (cnt+cero)), min(6, 7 - cnt)]

# 7 - 맞은개수 = 순위
# 1 2 3 4 5 6 - 순위
# 6 5 4 3 2 1 - 맞은 개수