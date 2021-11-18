#baekjoon_1024_수열의 합

#=== import module ===#
import math
#=== Function define ===#

#=== variable declare ===#
N = 0; L = 0; average = 0;
#=== main function ===#


N,L = map(int, input().split());

while(1):
  #L이 100보다 클 경우 종료
  if L > 100:
    print(-1);
    exit(0);

  tmpList = [];
  average = int(N/L);
  mid_index = math.ceil(L/2) -1; #1을 줄이는 이유는 index는 0부터 시작하기 때문에

  num = average - mid_index;
  if(num < 0): 
    result = -1;
    break; # 음의 정수는 조건에 부합하지 않음.
  for i in range(L):
    tmpList.append(num);
    num += 1;

  if N == sum(tmpList): #조건에 부합하는 배열 찾음
    result = tmpList;
    break;
  else: #못 찾았을 경우
    L += 1; #L증가

if str(type(result)) == "<class 'int'>":
  print(-1);
else:
  for num in result:
    print(num, end=' ');


  


