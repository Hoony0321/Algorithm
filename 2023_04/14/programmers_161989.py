#문제 정보
#programmers - 연습문제 - 덧칠하기 (난이도1)

# def solution(n, m, section):
#     answer = 0
    
#     while(len(section) > 0):
#         answer += 1
#         start = section[0]
#         end = start + m - 1
        
#         removeList = []
#         for area in section:
#             if(start <= area <= end):
#                 removeList.append(area)
#             else: break;
        
#         for elem in removeList:
#             section.remove(elem)
            
        
        
#     return answer


from collections import deque

def solution(n, m, section):
    answer = 0
    section = deque(section)
    
    while(len(section) > 0):
        answer += 1
        start = section[0]
        end = start + m - 1
        
        tmpSection = section.copy()
    
        for area in tmpSection:
            if area <= end : section.popleft()
            else: break
        
            
        
        
    return answer