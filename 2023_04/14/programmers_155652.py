# 문제 정보
# programmers_155652 - 연습문제 - 둘만의 암호


def solution(s, skip, index):
    answer = ''
    skipOrd = []
    for char in skip:
        skipOrd.append(ord(char))
    
    
    for char in s:
        nextOrd = ord(char)
        for _ in range(index):
            print(chr(nextOrd))
            nextOrd += 1
            if(nextOrd > 122): nextOrd -= 26

            while(True):
                if nextOrd in skipOrd:
                    nextOrd += 1
                    if(nextOrd > 122): nextOrd -= 26
                else: break
                    
        
        
        answer += chr(nextOrd)
    
    return answer

print(solution("y", "az", 1))