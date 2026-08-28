def solution(park, routes): #y, x 순으로 출력할것.    
    x, y = 0,0 # 시작지점
    H, W = len(park), len(park[0])
    obstacles = []
    for u in range(len(park)):
        if 'S' in park[u]:
            y = park[u].index('S')
            x = u
        if 'X' in park[u]:
            for v in range(len(park[u])):
                if 'X' == park[u][v]:
                    obstacles.append([u,v])
    
    way = {'E': (0,1), 'S':(1,0), 'W':(0,-1), 'N':(-1,0)}
    for r in routes:
        d, a = r.split(' ')[0], int(r.split(' ')[1])
        ndx, ndy = way[d][0]*a, way[d][1]*a
        #범위 초과 고려
        if (x+ndx < 0) or (x+ndx >= H) or (y+ndy >= W) or (y+ndy < 0):
            continue
        
        #장애물 확인
        minx, maxx = min(x, x+ndx), max(x, x+ndx)
        miny, maxy = min(y, y+ndy), max(y, y+ndy)
        for obs in obstacles:
            if (minx <= obs[0] <= maxx) and (miny <= obs[1] <= maxy): #중간에 장애물이 있다면
                #print(f'방향 {d}, 거리 {ndx, ndy}, 현재 위치 {x, y} 유지') 
                break
        else:
            #print(f'방향 {d}, 거리 {ndx, ndy}, 현재 위치 {x, y} 다음 위치 {x+ndx, y+ndy}')   
            x += ndx
            y += ndy
    
    return [x,y]