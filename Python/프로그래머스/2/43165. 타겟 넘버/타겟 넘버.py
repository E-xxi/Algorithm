def solution(numbers, target):
    leaves = [0]          # 모든 계산 결과를 담자      
    count = 0 

    for num in numbers : 
        temp = []
        for l in leaves:
            temp.append(l+num)
            temp.append(l-num)
        #print(temp)
        
        leaves = temp[:]
	
    #print(leaves.count(target))
    return leaves.count(target)