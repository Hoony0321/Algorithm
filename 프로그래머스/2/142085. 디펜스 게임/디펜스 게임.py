def canWin(stage, n, k, enemy):
    enemyList = enemy[:stage+1]
    enemyList.sort()
    
    return n >= sum(enemyList[:-k])

def solution(n, k, enemy):
    
    left = 0
    right = len(enemy)-1
    maxStage = -1
    
    while(left <= right):
        mid = (left + right) // 2
        
        if(canWin(mid, n, k, enemy)):
            maxStage = max(maxStage, mid)
            left = mid+1
        
        else:
            right = mid-1
    
    return maxStage+1