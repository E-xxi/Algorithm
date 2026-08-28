def solution(dots):
    x=[]
    y=[]
    width, height = 0,0
    for d in dots:
        x.append(d[0])
        y.append(d[1])
    
    x = sorted(x)
    y = sorted(y)
    return (x[-1]-x[0]) * (y[-1]-y[0])