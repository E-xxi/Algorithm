#문장 완성을 위한 단어조각의 개수
#dp는 항상 i 번째까지의 최적값에 뒤에꺼를 누적하는 방식!
# i 번째꺼까지 최소 값을 구해나가야돼?
def solution(strs, t):
    n = len(t)
    INF = float('inf')
    
    # word[i]: i지점까지 만드는데 필요한 최소 조각 수
    word = [INF] * (n + 1)
    word[0] = 0
    
    # setdefault: 키가 있으면 추가하고 아니면 새로 만듬
    by_len = {}
    for s in strs:
        by_len.setdefault(len(s), set()).add(s)
    print(by_len)
    
    lengths = by_len.keys()
    #  i
    #banana
    for i in range(1, n + 1):
        for L in lengths:
            if i >= L:
                sub = t[i-L:i]
                if sub in by_len[L]:
                    #i-L지점까지랑 비교해서 
                    word[i] = min(word[i], word[i-L] + 1)
    
    return word[n] if word[n] != INF else -1


#nabnabn
#: ab,na,bn,n,a
#na b na bn 
#
#na b na b n 
#n ab n ab n 
