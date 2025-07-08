def solution(n, w, num):
    answer = 0
    idx = num % w if num % w != 0 else w
    
    while(num <= n):
        answer += 1
        idx = num % w if num % w != 0 else w
        num += 2 * (w-idx) + 1
    
    
    return answer