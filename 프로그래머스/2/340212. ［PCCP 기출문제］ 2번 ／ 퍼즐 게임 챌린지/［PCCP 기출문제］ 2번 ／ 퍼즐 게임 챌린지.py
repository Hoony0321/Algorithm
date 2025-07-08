def solution(diffs, times, limit):
    answer = float('inf')
    n = len(diffs)
    left = 1
    right = max(diffs)
    
    def is_possible(level):
        total = 0
        for i in range(n):
            if diffs[i] <= level:
                total += times[i]
            else:
                total += (diffs[i] - level) * (times[i-1] + times[i]) + times[i]
            
            if total > limit:
                return False
        
        return True
    
    while left <= right:
        mid = (left + right) // 2
        
        if is_possible(mid):
            answer = min(mid, answer)
            right = mid - 1
        else:
            left = mid + 1
    
    return answer