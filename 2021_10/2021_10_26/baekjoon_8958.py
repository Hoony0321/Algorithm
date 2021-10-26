#baekjoon_8958 OX퀴즈

def ReturnQuizScore(case):
  score = 0;
  addValue = 0;
  for answer in case:
    if answer == 'X':
      addValue = 0;
    else:
      addValue += 1;
      score += addValue;
  
  return score;

test_case = int(input());

for case in range(test_case):
  quiz_result = input();
  
  score = ReturnQuizScore(quiz_result);
  print(score);