from collections import Counter
def solution(friends, gifts):
    N = len(friends)
    answer = [0] * N
    #더 많이 주면 하나 더 받음 - 선물지수 따라서 - 아니며 ㄴ안주고받음
    #선물지수: 준 선물 - 받은 선물 
    friends = {f: idx for idx, f in enumerate(friends)}
    legacy = [[0]* len(friends) for _ in range(N)] 
    gift_cnt = {f:0 for f in friends.values()}
    gifts = dict(Counter(gifts)).items()
    
    for who, cnt in gifts:
        a,b = friends[who.split()[0]], friends[who.split()[1]]
        legacy[a][b] = cnt
        gift_cnt[a] += cnt
        gift_cnt[b] -= cnt
    
    for i in range(N):
        for j in range(i+1, N):
            #주고 받은 적이 없으면
            if legacy[i][j] > legacy[j][i]:
                answer[i] +=1
            elif legacy[i][j] < legacy[j][i]:
                answer[j] += 1
            else: # 선물지수가 큰 사람이 get
                if gift_cnt[i] > gift_cnt[j]:
                    answer[i] += 1
                elif gift_cnt[i] < gift_cnt[j]:
                    answer[j] += 1
    
            
            
        
    return max(answer)