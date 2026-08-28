def solution(n, left, right): 
    answer = []
    
    #print((left//n, left%n), (right//n, right%n)) 
    for i in range(left//n,right//n+1):
        for j in range(n):          
            if (left//n,left%n) <= (i,j) <= (right//n,right%n) :         
                answer.append(max(i,j)+1)
    
    return(answer)

