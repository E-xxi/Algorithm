def solution(numbers):
    answer = []

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