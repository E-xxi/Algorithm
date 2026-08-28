from collections import deque

def solution(maps): #최
    dxy = [[1,0],[-1,0],[0,1],[0,-1]]
    N, M = len(maps), len(maps[0])
    queue = deque([[0,0,1]])   
    maps[0][0] = 0
    
    while queue:
        currx, curry, cnt = queue.popleft()
        
        if (currx == N-1) and (curry == M-1):
            return cnt
        
        for dx,dy in dxy:
            nx, ny = currx + dx, curry + dy
            if (-1 < nx <N) and (-1 < ny <M) and maps[nx][ny]:
                maps[nx][ny] = 0
                queue.append((nx,ny,cnt+1))
    
    return -1