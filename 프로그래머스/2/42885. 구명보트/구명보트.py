from collections import deque

def solution(people, limit):
    answer = 0
    
    people.sort()
    people = deque(people)
    
    while people:
        answer += 1
        minW, maxW = people[0], people[-1]
        
        if(minW + maxW > limit or len(people) == 1):
            people.pop()
        else:
            people.pop()
            people.popleft()
        
    
    
    return answer