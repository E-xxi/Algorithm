from collections import deque

def find_p(places):
    idx = []
    for i in range(5):
        for j in range(5):
            if places[i][j] == 'P':
                idx.append([i,j])
    return idx

def check(person_idxs, room):
    #print(person_idxs)
    dxy = [(1,0),(0,1),(-1,0), (0,-1)]
    
    while person_idxs:
        x,y = person_idxs.pop()

        for dx,dy in dxy:
            nx,ny = x+dx, y+dy
            if (0<=nx<5) and (0<=ny<5): #범위 안에 있고
                #테두리에 1이 하나라도 있으면 안돼
                # 1이 있는지 확인 -> 있으면 break
                #O는 빈테이블/ X는 파티션 
                if room[nx][ny] in ['1','P']: 
                    return 0
                elif room[nx][ny] == 'O':
                    room[nx][ny] = '1'
    return 1

def solution(places):
    answer = []    
    
    for rn in range(5):
        room = [list(row) for row in places[rn]]
        answer.append(check(find_p(room), room))
            
    
    return answer