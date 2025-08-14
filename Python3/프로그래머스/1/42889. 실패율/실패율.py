def solution(N, stages):#stages: 도달한 시점
    answer = []
    percentage = {}
    
    fail = [0]*(N+1)

    for h in stages:
        fail[h-1] += 1
    #print(fail)
    
    for i in range(N):
        try:
            percentage[i] = fail[i]/sum(fail[i:])
        except:
            percentage[i] = 0
        
    percentage = sorted(list(percentage.items()), key = lambda x:x[1], reverse = True)
    
    for p in list(percentage):
        answer.append(p[0]+1)
        
    #print(percentage)
    return answer