import heapq
def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    distances = [float('inf')]*(N+1)
    distances[1] = 0
    
    for a,b,c in road: # a-b 마을 번호 , c 걸리는 시간
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    
    heap = [] 
    #heap은 [0]값으로 오름차순 정렬
    heapq.heappush(heap,(0,1)) # (cost, node)입력
    while heap:
        dist, node = heapq.heappop(heap) #다음 최소값 반환
            
        for next_node, next_dist in graph[node]:
            cost = dist + next_dist
            if cost < distances[next_node]:
                distances[next_node] = cost
                distances[next_node] = cost
                heapq.heappush(heap,(cost,next_node))
    
    # 1인 개수 반환해서 더해주도록
    return sum(1 for dist in distances if dist <= K)