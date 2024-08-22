from collections import deque

def solution(people, limit):
    answer = 0
    
    people.sort()
    people = deque(people)
    
    while people:
        w1 = people.pop()
        
        if people and w1 + people[0] <= limit:
            people.popleft()
        
        answer += 1
    
    return answer