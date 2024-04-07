def solution(n):
    answer = []
    
    def hanoi(current, target, mid, n):
        if(n==1):
            answer.append([current, target])

        else:
            hanoi(current, mid, target, n-1)
            hanoi(current, target, mid, 1)
            hanoi(mid, target, current, n-1)
    
    hanoi(1,3,2,n)
    
    
    return answer