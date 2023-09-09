def canPass(num, stones, k):
    jumpCount = 0
    for stone in stones:
        if(stone < num):
            jumpCount += 1
            
            if jumpCount == k:
                return False
        else:
            jumpCount = 0
    return True
            

def solution(stones, k):
    if k == 1: return min(stones)

    left = 1
    right = max(stones)
    
    while(left  < right -1):
        mid = (left + right) // 2
        
        if canPass(mid, stones, k):
            left = mid
        else:
            right = mid
        
    return left