def find(parent, i):
    if parent[i] == i: #속한 곳이 없는 경우
        return i
    
    #제일 윗쪽까지 올라가서 부모 노드 설정
    parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    # 두 집합을 합치기
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    if rank[xroot] <  rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1
        
def solution(n, costs):
    # 모든 섬이 서로 통행 가능한 최소 비용
    # 최소 작은것 순서대로 더해나가도록
    costs.sort(key= lambda x: x[2])
    
    #각 노드의 부모를 추적 - 사이클 방지 목적
    parent = [i for i in range(n)] 
    rank = [0] * n
    
    min_cost = 0
    edges = 0
    
    for edge in costs:
        if edges == n-1: #최소 경로가 모두 더해졌다
            break
        
        #현재 간선의 노드가 속한 parent 찾기(== 집합이 있는지 찾기)
        x = find(parent,edge[0])
        y = find(parent, edge[1])
    
        if x!= y:
            union(parent, rank, x, y)
            min_cost += edge[2]
            edges +=1
            
    return min_cost