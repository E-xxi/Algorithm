def solution(num_list):
    answer = 1
    if len(num_list) >= 11:
        return sum(num_list)
    
    for n in num_list:
        answer *= n
    return answer
    