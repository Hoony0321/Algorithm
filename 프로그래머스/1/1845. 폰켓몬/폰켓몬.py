from collections import defaultdict
def solution(nums):
    answer = 0
    pocketDict = defaultdict(int)
    for num in nums:
        pocketDict[num] += 1
        
    n = len(nums) // 2
    return n if len(pocketDict.keys()) >= n else len(pocketDict.keys())