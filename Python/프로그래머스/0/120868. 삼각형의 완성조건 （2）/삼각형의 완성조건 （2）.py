def solution(sides):
    sides = sorted(sides) 
    return len([i for i in range(sides[1]-sides[0]+1, sum(sides))])