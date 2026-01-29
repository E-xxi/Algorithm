import functools

def compared(x, answer):
    return -1 if x not in answer else 1

def solution(s):
    #중복있음, 순서 인정
    answer = []
    #s가 표현하고 있는 튜플
    comb_nums = []
    for ch in s.split('}'):
        if ch != '':
            comb_nums.append(list(map(int, ch.split('{')[-1].split(','))))
    
    #일단 기본적으로 순서를 가지거 있었는데, 괄호 안의 숫자 숫서는 바뀜
    #전체를 구한 다음에 줄여나가면서 없는 숫자 가 마지막인듯
    #{3,2,4,1}부터 시작해서 num에 없는 숫자를 맨 뒤로?
    comb_nums.sort(key = lambda x:-len(x))
    answer = comb_nums.pop()
    for num in comb_nums[::-1]:
        for a in answer:
            try:
                num.pop(num.index(a))
            except:
                answer.append(a)
                break
        answer+=num
    # d
    
    
    
    
    return answer