#주요 포인트: // 사용
# 딕셔너리 순서가 바꼈을수도 있다는거
def solution(enroll, referral, seller, amount):
    answer = []
    # 본인 윗 루트들에게 10%씩 * 소숫점은 계산 안함
    # == 아래 루트들의 10%만큼 받은거의 10%로도 위로 분배해야됨
    root = dict(zip(enroll,referral)) 
    total = {e:0 for e in enroll}
    
    for i in range(len(seller)):
        money = amount[i] * 100 # 기준 금액 계산
        cur_name = seller[i]
        
        while money>0 and cur_name !='-':
            total[cur_name] += money - money // 10
            cur_name = root[cur_name]
            
            money //= 10
            
    return [total[name] for name in enroll]