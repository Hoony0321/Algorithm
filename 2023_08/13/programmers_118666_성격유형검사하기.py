def solution(survey, choices):
    answer = ''
    
    result = { 'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    personalCases = [['R','T'], ['C','F'], ['J','M'], ['A','N']]
    
    for idx, choice in enumerate(choices):
        if choice < 4 : #비동의 점수
            result[survey[idx][0]] += 4 - choice
        elif choice > 4 : #동의 점수
            result[survey[idx][1]] += choice - 4
    
    for case in personalCases:
        if(result[case[0]] >= result[case[1]]):
            answer += case[0]
        else:
            answer += case[1]
        
    
    return answer