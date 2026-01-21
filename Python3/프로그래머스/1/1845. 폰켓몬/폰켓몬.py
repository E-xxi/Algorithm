from collections import Counter
def solution(nums):
    n = len(nums)//2 # n 마리 선택
    difcnt = len(Counter(nums).keys()) #종류 개수
    return min(n, difcnt)