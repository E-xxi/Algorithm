def findNum(num, keypad):
    for i in range(4):
        if num in keypad[i]:
            return (i, keypad[i].index(num))

def solution(numbers, hand):
    answer = ''
    
    keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]    
    ldx,ldy = 3,0
    rdx,rdy = 3,2
    
    #print(keypad.index(5))
    
    for n in numbers:
        dx, dy = findNum(n, keypad)
        key = ''
        if n in [1,4,7]:
            key = 'L'
        elif n in [3,6,9]:
            key = 'R'
        else:
            ndx, ndy = findNum(n,keypad)
            
            leftDist = abs(ndx-ldx) + abs(ndy - ldy)
            rightDist = abs(ndx-rdx) + abs(ndy-rdy)

            if leftDist == rightDist:
                key = hand[0].upper()
            elif leftDist > rightDist: #오른손이 가깝
                key = 'R'
            else:
                key = 'L'
                
        answer += key
        if key == 'R':
            rdx, rdy = dx, dy
        else:
            ldx, ldy = dx, dy
    return answer