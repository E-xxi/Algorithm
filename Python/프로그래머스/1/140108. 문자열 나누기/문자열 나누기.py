def solution(s):
    answer = 0
    
    i, j = 0, 1
    cnt = 1
    while j <= len(s):
        if j >= len(s):
            answer +=1
            break
        
        if s[i] == s[j]:
            cnt += 1
        else:
            cnt -= 1
        j+=1
        
        if cnt == 0:
            #print(s[i:j])
            i, j = j, j+1
            answer+=1
            cnt = 1 
        #print(i, j, cnt)    
    return answer