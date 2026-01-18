def check_depth(target, lever, maps):
    N,M = len(maps), len(maps[0])   
    depth = 1
    tree_list = [lever]
    dxy = [(0,1),(0,-1),(1,0),(-1,0)]
    
    while tree_list:          
        temp = []
        for x,y in tree_list: #레버에서 내려가면서 확인
            maps[x][y] = 'X'
            for dx, dy in dxy: 
                if (0<=x+dx<N) and (0<=y+dy<M) and ((x+dx,y+dy) not in temp) :
                    if maps[x+dx][y+dy] == target:
                        return depth
                    elif maps[x+dx][y+dy] != 'X':
                        temp.append((x+dx,y+dy))
        tree_list = temp
        #print(tree_list)
        depth += 1 
    return 0

def solution(maps):
    answer = 0
    #레버를 기준으로 트리를 만들어서 
    #각각 start까지 뎁스 exit까지 뎁스를 구하면 될듯?
    maps = [list(row) for row in maps]
    
    for i in range(len(maps)):
        if 'L' in maps[i]:
            lever = i, maps[i].index('L')
    
    #maps.copy() 얕은복사때문에 충돌
    ls = check_depth('S', lever, [row[:] for row in maps])
    le = check_depth('E', lever,  [row[:] for row in maps]) 
    #print(ls,le)
    
    return ls+le if ls and le else -1