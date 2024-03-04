
def solution(n):
    answer = ""
    numDict = {0 : "4", 1 : "1", 2 : "2"}
    
    while(n > 0):
        rest = n % 3
        answer = numDict[rest] + answer
        if(rest == 0): n -= 1
        n //= 3    
    
    return answer