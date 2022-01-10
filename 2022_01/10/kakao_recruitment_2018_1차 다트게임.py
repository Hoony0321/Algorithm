#kakao_recruitment_2018_1차 다트게임

def solution(dartResult):
    answer = 0
    dartScores = [None, None, None];
    bonus = {'S' : 1, 'D' : 2, 'T' : 3};
    current = 0;
    idx = 0;
    while idx < len(dartResult):
      elem = dartResult[idx];
      if elem.isdigit(): #숫자인 경우
        if dartScores[current] == None:
          dartScores[current] = int(elem);
        else: #10점인 경우
          dartScores[current] = 10;
      else: #문자인 경우
        if elem in bonus: #보너스인 경우
          dartScores[current] = dartScores[current] ** bonus[elem];
          current += 1;
        elif elem == '*':
          if current != 1:
            dartScores[current-2] *= 2; 
          dartScores[current-1] *= 2;
        elif elem == '#':
          dartScores[current-1] *= -1;
      
      idx += 1;

    for elem in dartScores:
      answer += elem; 
        
    
    return answer
  

print(solution("1D2S#10S"));