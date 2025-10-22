def solution(wallet, bill):
    n = max(wallet)
    m = min(wallet)
    
    bill.sort()
    answer = 0
    
    def folding(a,b): # a must be smaller than b
        b //= 2
        return [a,b] if a < b else [b,a]
    
    while(bill[1] > n or bill[0] > m):
        bill = folding(bill[0],bill[1])
        answer += 1
        
    return answer