def solution(n, words):
    person = 1
    cnt = 1
    l = []
    last = words[0][0]
    for i in range(len(words)):
        person = i%n+1
        cnt = i//n+1
        if (words[i] in l) or (last != words[i][0]):
            return [person,cnt]
        l.append(words[i])
        last = words[i][-1]
    print('return')
    return [0,0]

