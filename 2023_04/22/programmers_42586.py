#문제 설명
#programmers_42586 - 기능개발 (난이도 2)

from collections import deque

def solution(progresses, speeds):
    answer = []
    
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while(progresses):
        
        #진도 증가
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        count = 0
        while(progresses):
            if(progresses[0] >= 100):
                progresses.popleft()
                speeds.popleft()
                count += 1
            else:
                break
        
        if(count > 0):
            answer.append(count)
    
    return answer