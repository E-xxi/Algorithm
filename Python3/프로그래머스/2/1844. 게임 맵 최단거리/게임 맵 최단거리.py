from collections import deque
def solution(maps):
    que = deque()
    que.append((0,0,1))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    w = len(maps)
    h = len(maps[0])
    while que:    
        i, j, dist = que.popleft()        
        if (i == w-1) and (j == h-1):
            return dist
        
        for x,y in zip(dx,dy):
            nx = x+i
            ny = y+j
            if (0<=nx<w) and (0<=ny<h) and (maps[nx][ny] == 1):
                maps[nx][ny] = 0 
                que.append((nx,ny,dist+1))
        
    return -1