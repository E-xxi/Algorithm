def solution(players, m, k): #m 증설시점, k 운영시간
    answer = 0

    server_cnt = 0 #현재 서버 개수
    server_time = {}
    
    for i in range(len(players)):
        #타임아웃된 서버 삭제
        if i-k in server_time.keys():
            server_cnt -= server_time[i-k]
        
        # 현재 필요한 서버 개수 
        if server_cnt < players[i]//m:
            cnt = players[i] // m - server_cnt
            answer += cnt
            server_time[i] = cnt #증설된 서버의 시간을 저장
            server_cnt = players[i] // m
        
        #print(i, f'~ {i+1}시간', server_cnt, answer)   
        
    return answer