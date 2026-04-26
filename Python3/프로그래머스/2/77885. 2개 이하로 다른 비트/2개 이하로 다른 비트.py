def solution(numbers):
    answer = []
    #비트가 2개 이하로만 다른거
    #1개만 다른거 - 가장 마지막 비트가 0이면 -> 1로 변환
    
    for num in numbers:
        b = ['0'] + list(bin(num)[2:])

        if b[-1] == '0': #가장 마지막 비트가 0이면 이거만 변환하면
            b[-1] = '1'
            answer.append(int(''.join(b),2))
        else: #뒤에서부터 가장 마지막 '01'을 swap
            b = b[::-1]
            idx = b.index('0')
            b[idx-1],b[idx] = b[idx],b[idx-1]
            answer.append(int(''.join(b[::-1]),2))
    
    return answer