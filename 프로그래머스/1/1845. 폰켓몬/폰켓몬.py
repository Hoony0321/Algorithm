from collections import defaultdict

def solution(nums):    
    pocketmons = defaultdict(int)
    
    for num in nums :
        pocketmons[num] += 1
    
    n = len(nums)
   
    return n // 2 if n // 2 <= len(pocketmons.keys()) else len(pocketmons.keys())