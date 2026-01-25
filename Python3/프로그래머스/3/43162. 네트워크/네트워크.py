def solution(n, computers):
    answer = 0
    visited = [-1]*n
    
    for i in range(n):
        if visited[i] == -1: #방문하지 않았다면
            #print(f'visit {i}')
            stack = [i]
            visited[i] = i
            computers[i][i] = 0
            
            while stack: #연결된것 찾기
                curr = stack.pop()
                #print('curr',curr,stack)
                visited[curr] = visited[i]
            
                for j in range(n):
                    computers[j][j] = 0
                    if computers[curr][j]: #연결시
                        #print('j',j)
                        stack.append(j)
                        computers[curr][j], computers[j][curr] = 0,0
                        visited[j] = visited[i]
                        
    print(visited)
                  
    return len(set(visited))