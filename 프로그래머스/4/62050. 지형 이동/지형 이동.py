import heapq

def make_land(land):
    N=len(land)
    min_val,x,y = 100000,0,0
    
    for i in range(N):
        for j in range(N):
            if land[i][j] < min_val:
                min_val,x,y=land[i][j],i,j
            land[i][j] = [land[i][j],False]
    return land,x,y

def is_valid(x,y,N):
    return (0<= x < N) and (0<= y < N)
    

def solution(land, height):
    answer = 0
    N = len(land)
    dxy = [(0,1),(1,0),(0,-1),(-1,0)]
    
    land,x,y = make_land(land)
    
    heap = []
    heapq.heappush(heap,[0,x,y]) #(사다리, X,Y)
    
    #우선 방문 가능한 것만 heap에 넣어놓자 #abs사용
    while heap:
        ladder, x,y = heapq.heappop(heap)
        if land[x][y][1]:
            continue
        land[x][y][1] = True
        answer += ladder
        #print(f'{x,y}, ladder: {ladder}')
        
        for dx,dy in dxy:
            nx,ny = x+dx,y+dy
            if is_valid(nx,ny,N) and not land[nx][ny][1]: #범위 내에 있는지
                diff = 0 if abs(land[nx][ny][0] - land[x][y][0]) <= height else abs(land[nx][ny][0] - land[x][y][0])
                heapq.heappush(heap,[diff,nx,ny]) #least하게 추가하는것
    return answer