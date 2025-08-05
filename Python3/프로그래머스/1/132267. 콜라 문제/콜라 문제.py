def solution(a, b, n):
    answer = 0
    # 빈병 a개 -> +b개를 돌려줌
    while n >= a:
        #print(n, n//a, answer)
        answer += n//a * b
        n = (n//a * b + n%a)       
    return answer

# 5 2 20 --- 8
# -> 8
# -> 3 + 2 --- 2
# -> ---2