#문제설명
#prgrammers_12900 - 2xn 타일링 (난이도 2)
from collections import deque

def solution(n):
    answer = [0]
    
    fibo = [0 for _ in range(n+1)]
    fibo[0], fibo[1], fibo[2] = 1,1,2
    
    if(n <= 2): return fibo[n]
    
    for i in range(3, n+1):
        fibo[i] = (fibo[i-2] + fibo[i-1]) % 1000000007
        
            
    return fibo[n]