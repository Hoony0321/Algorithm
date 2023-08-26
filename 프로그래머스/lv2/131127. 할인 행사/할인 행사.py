from collections import Counter
def solution(want, number, discount):
    answer = 0
    dict_want = dict()
    
    for i in range(len(want)):
        dict_want[want[i]] = number[i]
    
    for i in range(len(discount)-9):
        if dict_want == Counter(discount[i:i+10]):
            answer += 1
    
    return answer