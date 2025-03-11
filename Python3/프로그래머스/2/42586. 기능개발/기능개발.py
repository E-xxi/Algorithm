def solution(progresses, speeds):
    comp = [] #배포날짜
    answer = []
    for p,s in zip(progresses,speeds):
        k=1
        if (100-p)//s == (100-p)/s:
            k = 0
        comp.append((100-p)//s+k+1)
    print(comp)
    day = comp[0]
    cnt = 1
    for i in range(1,len(comp)):
        if comp[i] <= day:
            cnt+=1
        else:
            answer.append(cnt)
            day = comp[i]
            cnt=1
    answer.append(cnt)
    return answer