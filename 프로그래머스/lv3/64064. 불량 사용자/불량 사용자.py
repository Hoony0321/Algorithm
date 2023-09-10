import itertools

def find_available(user, target):
    if(len(user) != len(target)): return False

    for idx,elem in enumerate(user):
        if(target[idx] == '*'): continue
        if(target[idx] != elem): return False
    
    return True
    
        

def solution(user_id, banned_id):
    
    ban_list = []
    
    for ban in banned_id:
        tmp_list = []
        for user in user_id:
            if(find_available(user,ban)):
                tmp_list.append(user)
                    
        ban_list.append(tmp_list)
    
    combinations = list(itertools.product(*ban_list))
    result = set([])
    
    for elem in combinations:
        elem = frozenset(elem)
        if(len(elem) == len(banned_id)):
            result.add(elem)
            
    print(result)
    
    return len(result)