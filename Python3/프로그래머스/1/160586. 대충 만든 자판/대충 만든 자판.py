def solution(keymap, targets):
    answer = []
    
    for words in targets:
        cnt = 0
        for c in words:
            temp = 1000
            for key in keymap:
                if c in key:
                    temp = min(temp, key.index(c)+1)
            #print(c, temp)
            if temp < 1000:
                cnt += temp
            else:
                cnt = -1
                break
        answer.append(cnt)
            
    return answer