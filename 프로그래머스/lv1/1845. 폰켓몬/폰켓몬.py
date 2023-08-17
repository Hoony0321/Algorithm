def solution(nums):
    num_choice = len(nums)//2
    num_monster = len(set(nums))
    return num_monster if num_choice > num_monster else num_choice