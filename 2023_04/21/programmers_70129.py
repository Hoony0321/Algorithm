#문제정보
#programmers_

def solution(s):
    count = [0,0]
    
    while(s != "1"):
        count[0] += 1
        count[1] += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
    
    return count