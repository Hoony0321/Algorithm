def solution(n, s):
    if s < n : return [-1]
    answer = []

    while(n > 0):
        answer.append(s // n)
        s -= s // n
        n -= 1
    
    
    return answer