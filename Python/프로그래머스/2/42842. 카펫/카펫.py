def solution(brown, yellow):
    answer = []
    total = brown+yellow
    
    #테두리 한줄만 갈색이면
    #노란색이 : i-2,j-2이면 갈색은: i, j
    
    for i in range(3, int(total**(1/2))+1):
        if (total % i == 0):
            j = total // i
            if ((i-2) * (j-2)) == yellow:
                answer = [i,j]
    
    return sorted(answer,reverse = True)