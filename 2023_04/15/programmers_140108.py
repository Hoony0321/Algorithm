#문제정보
#programmers_140108 - 연습문제 - 문자열 나누기 (난이도 1)

def solution(s):
    answer = 0
    
    firstChar = ""
    firstCharCount = 0
    otherCharCount = 0
    
    for char in s:
        if(firstChar == ""):
            firstChar = char
            firstCharCount += 1
            continue
        else:
            if(firstChar == char):
                firstCharCount += 1
            else:
                otherCharCount += 1
                if(otherCharCount == firstCharCount):
                    firstChar = ""
                    firstCharCount = 0
                    otherCharCount = 0
                    answer += 1
    
    if firstChar != "": answer+=1 
        
        
    return answer