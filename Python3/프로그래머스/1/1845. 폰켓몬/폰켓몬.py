def solution(nums):
    answer = 0
    n = len(nums) // 2
    
    #print(set(nums))
    for i in range(len(set(nums))):
        answer+=1
        if n == answer:
            break
        
            
    return answer