from collections import Counter
def solution(participant, completion):
    p_dict = Counter(participant)
    c_dict = Counter(completion)
    
    for key,value in p_dict.items():
        if(c_dict[key] != value):
            return key