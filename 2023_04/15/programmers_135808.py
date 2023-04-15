#문제정보
#programmers_135808 - 연습문제 - 과일 징수 (난이도 1)

from collections import deque
    
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    score = deque(score)
    boxList = []
    
    while(len(score) >= m):
        box = []
        for _ in range(m):
            box.append(score.popleft())
        
        boxList.append(box)
        
    for box in boxList:
        answer += min(box) * len(box)
            
        
    
    return answer