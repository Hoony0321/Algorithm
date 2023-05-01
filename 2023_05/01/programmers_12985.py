#문제정보
#programmers_12985 - 예상 대진표 (난이도 2)

def solution(n,A,B):
    answer = 1
    
    matches = [[i,i+1] for i in range(1,n+1,2)]
    while(True):
        for index,match in enumerate(matches):
            p1, p2 = match
            if((p1 == A and p2 == B) or (p1 == B and p2 == A)):
                return answer
            elif(p1 == A or p2 == A):
                matches[index] = A
            elif(p1 == B or p2 == B):
                matches[index] = B
            else:
                matches[index] = p1
        
        tmpList = [[matches[i], matches[i+1]] for i in range(0,len(matches),2)]
        matches = tmpList
            
        answer += 1