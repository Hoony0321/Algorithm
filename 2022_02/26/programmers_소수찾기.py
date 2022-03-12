#baekjoon_

#=== import module ===#
from itertools import permutations
#=== variable declare ===#

#=== Function define ===#
def isPrime(num):
  if num in [0,1]:
    return False;
  
  for i in range(2,num):
    if num % i == 0: #나누어 떨어짐 -> 소수 아님
      return False;

  return True;
    


def solution(numbers):
  numList = list(map(int,list(numbers)));
  answer = set();
  for i in range(1,len(numList)+1):
    permuList = set(permutations(numList,i));
    for elem in permuList:
      num = 0;
      for i in range(len(elem)):
        num += elem[-i] * (10 ** i);
      if not isPrime(num) : continue;
      answer.add(num);

  return len(answer);
  

      
  
    
#=== main function ===#
print(solution("011"));

