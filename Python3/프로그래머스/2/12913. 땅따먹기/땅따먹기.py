import heapq
def solution(land):
    # 5,5,5,3
    # 5,6,7,8
    l = land[1][:]
    for i in range(1, len(land)):
        for j in range(4):
            m = max(land[i-1][:j]+land[i-1][j+1:])
            land[i][j] += m
            #print(i,j,m)
            #print(land[i])
    #print(land)
    return max(land[-1])
    