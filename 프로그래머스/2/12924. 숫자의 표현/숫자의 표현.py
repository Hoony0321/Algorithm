def solution(n):
    answer = 0
    
    for num in range(1,n+1):
        numSum = 0
        
        while numSum < n:
            numSum += num
            num += 1
            
        if numSum == n:
            answer += 1
    
    return answer