def solution(ineq, eq, n, m):
    if ineq == '>':
        if (eq == '=') and (n >= m):
            return 1
        elif (eq == '!') and (n > m):
            return 1
    else:
        if (eq == '=') and (n <= m):
            return 1
        elif (eq == '!') and (n < m):
            return 1
    return 0