def solution(myString, pat):
    answer = 0
    if pat.lower() in myString.lower():
        return 1
    
    return 0