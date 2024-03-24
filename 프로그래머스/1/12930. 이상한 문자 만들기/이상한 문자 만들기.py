def solution(s):
    answer = ''
    
    splitedString = s.split(' ')
    
    for string in splitedString:
        for i in range(len(string)):
            if(i % 2 == 0):
                answer += string[i].upper()
            else:
                answer += string[i].lower()
        answer += ' '
    
    return answer[:-1]