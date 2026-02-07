def solution(board):
    N,M = len(board), len(board[0])
    n = 0
    checked = [[0]*M for _ in range(N)] 
    
    #사각형 단위의 지형이동이라고 생각하고 ? 
    # 지형이동이라은 다른듯
    for i in range(N):
        for j in range(M):
            if board[i][j]: 
                if i==0 or j==0:
                    checked[i][j] = 1

                else:
                    checked[i][j] = min(checked[i-1][j-1], checked[i][j-1], checked[i-1][j])+1
                    
                n = max(checked[i][j], n)
    
    #for row in checked:
    #   print(row)

    return n**2