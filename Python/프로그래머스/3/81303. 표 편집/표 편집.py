def solution(n, k, cmd):
    deleted = []
    
    #링크드리스트 만드는 것
    #각 인덱스별로 위 아래 인덱스를 저장
    up = [i-1 for i in range(n+2)]
    down = [i+1 for i in range(n+1)]
    # e.g. 1 : up:0, down:2 저장
    
    #    0 1 2를
    # -1 0 1 2로 바꾼거라서 인덱스가 +1인 상태
    k += 1 
    
    for c in cmd:
        if c[0] == 'C':
            deleted.append(k)
            #지웠을때 바꿔야하는것
            #7라고 가정시, 
            # 1. 6(7의 위)의 down: 8
            # 2. 7(6의 다운)의 up: -
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            
            # 가장 마지막행일때는 k를 앞으로 아니면 밑에껄로 연결
            k = up[k] if down[k] > n else down[k]
            
        elif c[0] == 'Z':
            revoke = deleted.pop()
            # 2라면, 
            # 1. 1의 다운 = k
            down[up[revoke]] = revoke
            # 2. 3의 업은 k
            up[down[revoke]] = revoke
            # 2는 연결에서 끝났을때로 돌어가는거라서 따로 안해줘도 됨
        else: 
            di, num = c.split(' ')
            if di == 'U':
                for _ in range(int(num)):
                    k = up[k] #링크드리스트 타고 횟수만큼 올라가기
            else:
                for _ in range(int(num)):
                    k = down[k] 
    
    answer = ['O']*n
    for d in deleted:
        answer[d-1] = 'X'
    
    return ''.join(answer)