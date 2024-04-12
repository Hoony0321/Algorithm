def solution(d, budget):
    for i in range(len(d)-1):
        target = d[i]
        for j in range(i+1, len(d)):
            if(target > d[j]):
                target, d[j] = d[j], target
        
        d[i] = target
            
    
    answer = 0
    
    for cost in d:
        if(budget >= cost):
            budget -= cost
            answer += 1
        else:
            break;
    
    
    return answer