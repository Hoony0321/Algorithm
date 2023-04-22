#문제정보
#programmers_42747 - 정렬 (난이도 2)

def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    maxIndex = len(citations)
    
    while(maxIndex >= 0):
        if(citations[maxIndex-1] >= maxIndex):
            answer = maxIndex
            break
        maxIndex -= 1
    
    return answer