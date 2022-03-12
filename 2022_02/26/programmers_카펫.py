#baekjoon_

#=== import module ===#
from itertools import combinations, permutations
#=== variable declare ===#

#=== Function define ===#

def solution(brown, yellow):
  answer = [];
  row = 1; col = 1;

  while(1):
    if yellow % col == 0: #나누어 떨어짐
      row = yellow // col;
      if (row+2) * 2 + 2 * col == brown:
        answer = [row+2,col+2];
        break;
    
    col += 1;

  return answer;
    

#=== main function ===#
print(solution(8,1));

