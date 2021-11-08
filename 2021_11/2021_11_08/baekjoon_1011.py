#baekjoon_1011_Fly me to the Alpha Centauri
import math



def ReturnMinOperator(distance):
  count = 0;

  root_num = math.floor(math.sqrt(distance));
  square_num = root_num ** 2;
  diff = root_num;

  if distance == square_num:
    count = root_num * 2 - 1;
  elif distance > square_num + diff:
    count = root_num * 2 + 1;
  elif distance > square_num and distance <= square_num + diff:
    count = root_num * 2;
  
  if distance < 4:
    count = distance
  
  return count;





#=== 입력 ===#
test_case = int(input());

for case in range(test_case):
  startPoint, endPoint = map(float,input().split());
  distance = endPoint - startPoint
  #=== 풀이 ===#
  minOperator = ReturnMinOperator(distance);
  print(int(minOperator));



