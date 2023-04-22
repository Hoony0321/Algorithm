#문제정보
#programmers_12981 - 영어 끝말잇기 (난이도 2)

def solution(n, words):
    answer = [0,0]
    useList = dict()
    
    prev = words[0]
    useList[prev] = 1
    for i in range(1, len(words)):
        if(prev[-1] != words[i][0]): #첫,끝 알파벳 일치하지 않는 경우
            turn = (i+1) % n if (i+1) % n else n
            count = (i+1) // n + 1 if (i+1) % n else (i+1) // n
            answer = [turn, count]
            break
        
        if words[i] in useList: #사용한 적이 있는 단어
            turn = (i+1) % n if (i+1) % n else n
            count = (i+1) // n + 1 if (i+1) % n else (i+1) // n
            answer = [turn, count]
            break
        
        useList[words[i]] = 1
        prev = words[i]

    return answer