def solution(n,a,b):
    answer = 1
    
    #몇번째 라운드에 만나는가
    l = [1 if i+1 in [a,b]  else 0 for i in range(n) ]
    
    
    for i in range(n//2+1):
        #확인
        for k in range(0,len(l),2):
            if l[k] and l[k+1]:
                return answer
            
        l = [1 if l[j] or l[j+1] else 0 for j in range(0,len(l),2)]
        answer += 1
        
    return answer

'''
	[0, 0, 0, 1, 0, 0, 1, 0]
    [0,    1,    0,    1    ]
'''