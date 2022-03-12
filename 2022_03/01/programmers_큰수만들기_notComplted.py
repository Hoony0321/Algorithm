#programmers_greedy_큰 수 만들기

#=== import module ===#

#=== variable declare ===#

#=== Function define ===#
def solution(number, k):
  number = list(map(int,list(number)));
  visited = [False for _ in range(len(number))];
  while k > 0:
    preK = k; #변경된 문자가 있는 지 확인하기 위한 변수
    for idx in range(0,len(number)-1):
      if visited[idx]: continue;
      if int(number[idx]) < int(number[idx+1]):
        del number[idx];
        k -= 1;
        break;
      else:
        if number[idx] > max(number.slice):
          visited[idx] = True;

        

    if preK == k:
      for _ in range(preK):
        del number[-1]; #맨 마지막 숫자 계속해서 삭제
        k -= 1;

  answer = "";
  for elem in number:
    answer += str(elem);
  return answer;
  

#=== main function ===#
print(solution("41776543252841",5));

