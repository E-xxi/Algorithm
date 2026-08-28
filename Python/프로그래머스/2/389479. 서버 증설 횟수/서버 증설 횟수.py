def solution(players, m, k):
    answer = 0
    server = [0]*24 #시점,개수
    
    for i in range(24):
        if i-k >= 0 :
            server[i-k] = 0
        
        #필요한 서버만큼 추가 
        if players[i] // m > sum(server):
            add_server = players[i] // m - sum(server)
            server[i] = add_server
            answer += add_server
            #print(i,': ', players[i], sum(server), add_server)
        
        
    return answer