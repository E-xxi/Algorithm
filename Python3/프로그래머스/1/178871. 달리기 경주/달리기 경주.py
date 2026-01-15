#스왑하니까 시간초과
def solution(players, callings):
    rank = {n:idx for idx, n in enumerate(players)}
    
    for name in callings:
        i = rank[name] #현재 등수 리턴
        rank[name] -= 1
        rank[players[i-1]] += 1
        players[i],players[i-1] = players[i-1], name  
        
    return players