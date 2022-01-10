#kakao_recruitment_2018_1차 캐시
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque();
    
    if cacheSize == 0:
        return len(cities) * 5;
    
    for city in cities:
        city = city.lower(); #대소문자 무시
        if city in cache: #hit한 경우
            answer += 1;
            cache.remove(city);
            cache.appendleft(city);
        else: #miss한 경우
            answer += 5;
            if len(cache) == cacheSize: #맨 마지막 원소 삭제
                cache.pop();
            cache.appendleft(city); #맨 앞에 원소 추가
            
    
    return answer

## 좀 더 빠른 풀이 maxlen 사용

# def solution(cacheSize, cities):
#     answer = 0
#     cache = deque(maxlen=cacheSize);
    
#     for city in cities:
#         city = city.lower(); #대소문자 무시
#         if city in cache: #hit한 경우
#             answer += 1;
#             cache.remove(city);
#             cache.append(city);
#         else: #miss한 경우
#             answer += 5;
#             cache.append(city); #원소 추가
            
    
#     return answer


print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]));