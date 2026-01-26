from collections import deque
def find_index(target, maps):
    for idx, row in enumerate(maps):
        if target in row:
            return (idx,row.index(target))

def is_valid(x,y, maps):
    N,M = len(maps), len(maps[0])
    return (0<=x<N) and (0<=y<M) and (maps[x][y] != 'X')

def find_target(L, target, maps):
    #최단거리니까 bfs
    
    q = deque([[L[0],L[1],1]])
    dxy = [(0,1),(0,-1),(1,0),(-1,0)]
    
    while q:
        cx, cy, cnt = q.popleft()
        #print(cx,cy,cnt)
        
        for dx,dy in dxy:
            nx, ny = cx+dx, cy+dy
            if is_valid(nx,ny, maps): #지나갈수 있으면
                if maps[nx][ny] == target:
                    return cnt
                q.append((nx,ny,cnt+1))
                maps[nx][ny] = 'X'
    else:
        return 0
    
    
    return cnt

def solution(maps):
    answer = 0
    maps = list(map(list, maps)) #리스트로 변환
    
    lever = find_index('L',maps)
    
    #L-> S
    start = find_target(lever, 'S',[m[:] for m in maps])
    end = find_target(lever, 'E',[m[:] for m in maps])
    

    return start+end if start and end else -1