#문제정보
#programmers_42885 - 구명보트 (난이도 2)

from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    
        
    
    while len(people) > 1:
        minW, maxW = people[0], people[-1]
        
        if(minW + maxW > limit): #제한 몸무게 초과
            people.pop()
        
        else: #제한 몸무게 초과 X
            people.popleft()
            people.pop()
        
        answer += 1
        
    if(people): answer +=1 
    
    
    return answer