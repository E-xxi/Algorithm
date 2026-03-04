import numpy as np
def solution(board, skill):
    #skill 부분만 돌아가면서 값을 가질까
    N,M = len(board), len(board[0])
    change = {1:-1, 2:1}
    update = [[0]*(M+1)for _ in range(N+1)]
    
    #이렇게해야 board 전체에 다 방문하지 않고도 해결이 됨
    for type, r1, c1, r2, c2, degree in skill:
        update[r1][c1] += degree*change[type]
        update[r1][c2+1] += degree*change[type]* -1
        update[r2+1][c1] += degree*change[type]* -1
        update[r2+1][c2+1] += degree*change[type]
    #5  0 0 -5
    #0  0 0 0
    #0  0 0 0
    #-5 0 0 5
    for i in range(N+1):
        for j in range(1, M+1):
            update[i][j] += update[i][j-1]
            
    for i in range(1, N+1):
        for j in range(M+1):
            update[i][j] += update[i-1][j]
    
    answer = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] + update[i][j] > 0:
                answer += 1
                
    return answer

'''효율성 실패
    answer = len(board)*len(board[0])
    #파괴되지 않은 건물의 개수 
    change = {1:-1, 2:1}
    board = {idx:row for idx, row in enumerate(board)}
    
    for type, r1, c1, r2, c2, degree in skill:
        for r in range(r1,r2+1):
            for c in range(c1,c2+1):
                before = board[r][c]
                board[r][c] += degree*change[type]
                if (before > 0) and (board[r][c] <= 0): #공격받아서 파괴
                    answer -= 1
                elif (before <= 0) and (board[r][c] > 0):
                    answer += 1'''