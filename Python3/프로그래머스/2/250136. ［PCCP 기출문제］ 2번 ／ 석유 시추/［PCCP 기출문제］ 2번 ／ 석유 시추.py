from collections import defaultdict
def solution(land):
    
    '''
    시추관을 수직으로 하나만 뚫어서, 가장 많은 석유를 뽑을 수 있도록.
    #y기준으로 확인
    
    dfs돌때, 열마다 저장을 해놓아야되나?
    '''
    N, M= len(land), len(land[0])
    answer = [0 for o in range(M)]
    
    def is_valid(nx,ny):
        if 0 <= nx < N and 0 <= ny < M and land[nx][ny] == 1:
            return True
        
        return False
    
    #petrol_range: num각 석유가 위치한 컬럼의 범위
    #petrol_size: num각 얼마나 가지고 있는지
    column_num = defaultdict(set)
    petrol_size = defaultdict(lambda:1) #초기값 1로 설정
    
    def dfs(num,a,b):
        s = [(a, b)]
        land[a][b] = -1
        
        dxy =[(0,-1), (-1,0), (0,1) , (1,0)]
        
        while s: #연결되어있으면 같은 숫자로 칠하게 
            x, y  = s.pop()
            
            for dx,dy in dxy:
                nx, ny = x+dx,y+dy
                
                if is_valid(nx,ny): #범위 안이고, 방문하지 않은 land
                    if land[nx][ny] == 1: #석유 존재
                        column_num[ny].add(num)
                        petrol_size[num] += 1  
                        
                    s.append((nx,ny))
                    land[nx][ny] = -1
                    

    num = 1
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1:
                column_num[j].add(num)  #첫방문지도 포함해야됨
                dfs(num, i, j)
            num+=1
        
    #print(f'size: {dict(sorted(petrol_size.items()))}')
    #print(f'range: {dict(sorted(column_num.items()))}')
    
    for c,v in column_num.items():
        for idx in list(v):
            answer[c] += petrol_size[idx]
    
    return max(answer)