def solution(bandage, health, attacks):
    # bandage는 [시전 시간, 초당 회복량, 추가 회복량]
    hp = health
    heal_cnt = 0
    t = 0
    for idx, row in enumerate(attacks):
        #힐
        heal_cnt = row[0] - t - 1
        
        hp += heal_cnt*bandage[1]
        if heal_cnt >= bandage[0]:
            hp += bandage[2]*(heal_cnt//bandage[0])
        hp = min(health, hp)
            
        #공격
        hp -= row[1]
        
        #초기화   
        t = row[0]
        print(row[0], 'attack', hp)
        
        if hp <= 0:
            return -1
        
    return hp #캐릭터가 생존할 수 있는지