from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    
    success = True
    for word in goal:
        if len(cards1) > 0 and word == cards1[0]: cards1.popleft()
        elif len(cards2) > 0 and word == cards2[0]: cards2.popleft()
        else : 
            success = False
            break
    
    if(success): answer="Yes"
    else: answer="No"
    
    
    return answer