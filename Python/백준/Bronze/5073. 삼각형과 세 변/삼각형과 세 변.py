while True:
    l = sorted(list(map(int, input().split())), reverse = True) 
    if sum(l)== 0:
        break
    
    # a 가 빗변
    if l[0] >= l[1]+l[2]:
        print('Invalid')
    elif l[0] == l[1] == l[2]:
        print('Equilateral')
    elif (l[0] == l[1]) or (l[0] == l[2]) or (l[1] == l[2]): ## 5 3 3 이 경우도 고려
        print('Isosceles')
    else:
        print('Scalene')