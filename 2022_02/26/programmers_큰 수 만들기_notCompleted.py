#programmers_큰 수 만들기

#=== import module ===#
from itertools import combinations
#=== variable declare ===#

#=== Function define ===#
def solution(number, k):
  number = list(number);
  idxList = [i for i in range(len(number))];
  combList = set(combinations(idxList,k));

  max_result = 0;
  answer = "";
  for elem in combList:
    num = "";
    for idx in range(len(number)):
      if idx in elem: continue;
      num += number[idx];
    if max_result < int(num):
      max_result = int(num);
      answer = num;



  return answer;
      
    
    

#=== main function ===#
print(solution("4177252841",3));



