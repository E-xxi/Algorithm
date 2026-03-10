from itertools import combinations

def solution(n, q, ans):
    answer = 0

    que = list(combinations([i for i in range(1,n+1)],5))
    
    while que:
        numbers = que.pop()
        
        for cmp_n, an in zip(q,ans):
            cnt = 0
            for n in numbers:
                if n in cmp_n:
                    cnt+=1
            if cnt != an:
                break
        else:
            #print(numbers)
            answer+=1
    
    
    return answer
