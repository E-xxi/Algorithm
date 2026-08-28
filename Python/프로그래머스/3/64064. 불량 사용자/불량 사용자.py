from itertools import product

def is_match(user, banned):
    if len(user) != len(banned):
        return False
    for u, b in zip(user, banned):
        if b != '*' and u != b:
            return False
    return True


def solution(user_id, banned_id):
    possible = [] # 같은 제재 아이디가 있어서 딕셔너리는 안돼
    for banned in banned_id:
        temp = []
        for user in user_id:
            if is_match(user, banned):
                temp.append(user)
        possible.append(temp)
    #print(possible)
    
    result = set()
    #카타시안 곱으로 가능한 모든 경우의 수 
    for comb in product(*possible): 
        if len(set(comb)) == len(banned_id): #frodo, frodo, abc123 이런거 제거 
            #print(comb)
            result.add(frozenset(comb)) #frozenset : 집합 안의 집합으로 저장
        
    return len(result)
    