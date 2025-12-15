from collections import defaultdict
def solution(a):
    answer = -1
    a_dict = defaultdict(list)
    
    for i,num in enumerate(a):
        a_dict[num].append(i) 
    
    for k,v in a_dict.items():
        if answer >= len(v) * 2: continue
        
        cnt = 0
        _a = a.copy()
        for i in v:
            if i > 0 and _a[i-1] != k:
                cnt += 2
                _a[i-1] = k
            elif i < len(_a)-1 and _a[i+1] != k:
                cnt += 2
                _a[i+1] = k
        
        answer = max(answer, cnt)
    
    return answer