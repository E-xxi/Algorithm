from collections import Counter
def fill(b,n,i,j, cnt):
    dx = [-1, 0, 1,-1,1,-1,0,1]
    dy = [-1,-1,-1, 0,0, 1,1,1 ]
    
    for x,y in zip(dx,dy):
        nx = i+x
        ny = j+y
        if (0<=nx<n) and (0<=ny<n) and b[nx][ny] == 0:
            #print(nx,ny)
            b[nx][ny] = 2 
            cnt +=1
    return b, cnt+1


def solution(board):
    n = len(board)
    answer = 0 
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1: ## 지뢰가 있음
                #print(answer)
                board,answer = fill(board,n,i,j,answer)
    return n*n - answer