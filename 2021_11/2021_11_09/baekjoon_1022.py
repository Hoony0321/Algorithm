#baekjoon_1022_소용돌이 예쁘게 출력하기
#=== import module ===#
import math

#=== Function define ===#
def ReturnNumWhirl(point):
  return point[1];


#=== variable declare ===#
row1 = 0; row2 = 0; col1 = 0; col2 = 0;
lengthRow = 0; lengthCol = 0;
whirlpool = [];
direction_array = [[-1,0] , [0,-1], [1,0], [0,1]];
#=== main function ===#
row1,col1,row2,col2 = map(int,input().split());

lengthRow = row2 - row1 +1;
lengthCol = col2 - col1 +1;
whirlpool = [[0 for __ in range(lengthCol)] for _ in range(lengthRow)];

inputVal = 1; #들어가는 값.
point = [0,0] #들어가는 위치
if row1 <= 0 <= row2 and col1 <= 0 <= col2:
  whirlpool[0 - row1][0 - col1] = 1;
direction = 3;
leftTurn = 0;
numWhirl = 0;

#소용돌이 그리기
while(1):
  inputVal += 1;
  if leftTurn == 0: #방향을 바꿔야 함.
    if direction == 3: #새로운 바퀴 시작
      point[1] += 1;
      numWhirl = ReturnNumWhirl(point);
      direction = 0;
      leftTurn = numWhirl * 2 - 1;
    else: 
      direction = (direction+1)  % 4;
      point[0] += direction_array[direction][0]
      point[1] += direction_array[direction][1]
      leftTurn = numWhirl * 2 -1;
  else: #방향을 바꿀 필요 없음.
    leftTurn -= 1;
    point[0] += direction_array[direction][0]
    point[1] += direction_array[direction][1]

  #현재 point 
  #point가 넣어야 할 범위 안이면 입력
  if row1 <= point[0] <= row2 and col1 <= point[1] <= col2:
    whirlpool[point[0] - row1][point[1] -col1] = inputVal;

  #whirlpool이 다 채워졌는지 확인
  finish = True;
  for row in whirlpool:
    if 0 in row:
      finish = False;
      break;
  
  if finish:
    break;
  

maxLength = len(str(inputVal));
for row in whirlpool:
  for num in row:
    printNum = str(num);
    print(' '*(maxLength-len(printNum)) + printNum, end=' ');
  print();

  




