def solution(n, w, num):
    g = n//w
    #num위치 확인하기
    l = [i*w for i in range(1,g+1)] #층
    
    if not l:
        h = 0
    else:
        for h in range(len(l)):
            if num <= l[h]:
                break
    
    #* 몇층인지 알아내기
    if h % 2: #홀수층
        width = l[h] - num
    else: # 짝수층 
        width = num - (h+1)*w + (w-1)
    answer = g - (h+1)

    m = n%w
    # 맨 윗층이 있는지 없는지
    if g % 2: #홀수층
        if w - m <= width:
            answer+=1 
    else:
        if width + 1 <= m:
            answer += 1
    
    return answer +1

