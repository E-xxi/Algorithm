from collections import deque
def solution(n, edge):
    answer = 0
    #각 엣지마다 연결된 엣지들을 다 저장
    tree = [[] for _ in range(n+1)]
    
    for a, b in edge:
        tree[a].append(b)
        tree[b].append(a)
    
    visited = [0] * (n+1)
    visited[1] = 1
    q = deque([1])
    parent =  [0] * (n+1)
    dist = {i:0 for i in range(n+1)}
    
    while q:
        now = q.popleft()
        for nxt in tree[now]:
            if not visited[nxt]:
                visited[nxt] = 1
                parent[nxt] = now
                dist[nxt] = dist[now] +1
                q.append(nxt)
    
    dist = dict(sorted(dist.items(), key = lambda x:x[1], reverse = True))
    m = max(dist.values())
    
    
    for idx, d in dist.items():
        #print(idx, d)
        if d == m:
            answer +=1
        else:
            break
    
    
    return answer