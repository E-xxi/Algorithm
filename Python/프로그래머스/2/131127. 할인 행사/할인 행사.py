from collections import Counter
def solution(want, number, discount):
    answer = 0 #회원가입 가능한 기간. 
    # 금액 -> 10일 동안 회원자격, 매일 한 가지 제품 할인
    # 원하는 제품 할인 제품과 날짜가 10일 연속 일치 -> 회원가입
    
    want_items = {w:n for w,n in zip(want, number)}
    for i in range(len(discount)-9):
        discount_items = Counter(discount[i:i+10])

        if want_items == discount_items:
            answer += 1
    
    return answer