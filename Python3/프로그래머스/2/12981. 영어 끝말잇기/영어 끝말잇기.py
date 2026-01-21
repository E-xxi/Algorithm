def solution(n, words):
    word_list = []
    
    for idx, word in enumerate(words):
        if word_list: #두번째 차례부터
            if word[0] != word_list[-1][-1]: #잘못되 단어를 말했거나
                break
            elif len(set(word_list)) == len(set(word_list + [word])): #이전에 등장했던 단어거나     
                break
        word_list.append(word)
        
    else: #탈락자 없으면 
        return [0, 0]
    
    return [idx%n +1, idx//n +1]