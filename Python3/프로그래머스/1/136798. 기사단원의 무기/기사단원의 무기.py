def solution(number, limit, power):
    weapon_l = [1]
    #약수의 개수 
    for i in range(2,number+1):
        l = set()

        for j in range(1, int(i**(1/2))+1):
            if i % j == 0:
                l.add(j)
                l.add(i//j)
        if len(l) > limit:
            weapon_l.append(power)
        else:
            weapon_l.append(len(l))
    
    return sum(weapon_l)

