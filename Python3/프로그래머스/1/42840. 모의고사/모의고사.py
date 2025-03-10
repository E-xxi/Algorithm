def solution(answers):
    answer = []
    cnt = [0,0,0]
    num1 = [1,2,3,4,5] 
    num2 = [2,1,2,3,2,4,2,5] 
    num3 = [3,3,1,1,2,2,4,4,5,5] 
    
    for i in range(len(answers)):
        if answers[i] - num1[i%5] == 0:
            cnt[0] +=1
        if answers[i] - num2[i%8] == 0:
            cnt[1] +=1
        if answers[i] - num3[i%10] == 0:
            cnt[2] +=1
    
    m = max(cnt)
    for i in range(len(cnt)):
        if cnt[i] == m:
            answer.append(i+1)  
    return answer