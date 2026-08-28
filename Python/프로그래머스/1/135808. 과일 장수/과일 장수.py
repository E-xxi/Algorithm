def solution(k, m, score):
    #k가 맥스 점수 / m이 박스 당 개수 
    answer = 0
    score = sorted(score, reverse = True)[:len(score)//m*m]
    #print(score)
    
    # 박스당 최저가 얼마인지로 
    for i in range(m-1,len(score)+1,m):
        answer += score[i] * m
    
    return answer
        
