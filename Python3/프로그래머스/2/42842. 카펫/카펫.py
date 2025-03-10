def solution(brown, yellow):
    #print(bro)
    for i in range(1, brown//2+1): #가로
        for j in range(1, brown//2+1):
            if (yellow == (i-2)*(j-2)) and (brown == (i*j - (i-2)*(j-2))):
                return [max(i,j), min(i,j)]
    
    
    