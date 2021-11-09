#baekjoon_1025_제곱수 찾기
import math
import copy

#=== 함수 ===#

#selectedNum 배열에 있는 숫자를 하나로 만들고 SquareNum인지 판별 후 max_squareNum과 비교
def isSquareNum(selectedNum):
  global max_squareNum
  #selectedNum 리스트에 저장된 숫자를 하나의 숫자로 만들기
  result = "";
  for num in selectedNum:
    result += str(num);
  result = int(result);

  #squareNum 판별
  if math.sqrt(result).is_integer():
    #max_squareNum과 비교
    if max_squareNum < result:
      max_squareNum = result;

#=== 선언 ===#
row = 0; col = 0;
startPoint = [];
secondPoint = [];
otherPoint =[];
selectedNum = [];
diff = [];
table = [];
max_squareNum = -1;


#=== 입력 ===#
row, col = map(int,input().split());
for _ in range(row):
  tmpList = list(map(int,list(input())));
  table.append(tmpList);

#=== 풀이 ===#
#1개 선택


#2개 이상 선택
#startPoint 선택
for i in range(row):
  for j in range(col):    
    startPoint = [i,j];
    first_selectedNum = [table[startPoint[0]][startPoint[1]]]; #selectedNum배열 초기화
    isSquareNum(first_selectedNum); #max_squareNum비교

    #secondPoint 선택
    for p in range(row):
      for q in range(col):
        diff = []; #diff 초기화
        selectedNum = copy.deepcopy(first_selectedNum);#selectedNum 초기화

        if p == i and q == j: continue; #같은 칸은 피해야지.
        secondPoint = [p,q];
        selectedNum.append(table[p][q]); #selectedNum배열에 추가
        isSquareNum(selectedNum); #max_squareNum비교
        diff = [p-i, q-j]; #등차 결정.

        otherPoint = secondPoint;
        #otherPoint 선택
        while(1):
          y = otherPoint[0] + diff[0];
          x = otherPoint[1] + diff[1];
          if y < 0 or y >= row or x >= col or x < 0: break; #범위 넘어가면 루프 탈출

          otherPoint = [y,x];
          selectedNum.append(table[y][x]); #selectedNum배열에 추가
          isSquareNum(selectedNum); #max_squareNum비교


print(max_squareNum);
