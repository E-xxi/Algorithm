from itertools import permutations
def solution(k, dungeons):
    answer = -1
    cnt = 0

    dungeons = sorted(dungeons,key=lambda x: x[0],reverse = True)
    #print(list(permutations(dungeons,len(dungeons))))
    dl = list(permutations(dungeons,len(dungeons)))
    
    for dungeon in dl:
        cnt = 0
        hp = k
        for row in dungeon:
            if hp < row[0]:
                break
            hp-=row[1]
            cnt += 1       
        #print(dungeon,cnt)
                
        if cnt > answer:
            answer = cnt
            
    return answer