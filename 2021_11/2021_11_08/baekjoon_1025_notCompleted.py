#baekjoon_1025_제곱수 찾기
import math

#=== 함수 ===#
def isSquareNum(num):
  if math.sqrt(num).is_integer(): 
    return True;
  else: return False;

#=== 선언 ===#
row = 0; col = 0;
startPoint = [];
secondPoint = [];
otherPoint =[];
selectedNum = [];
diff = [];
table = [];
max_squareNum = 0;


#=== 입력 ===#
row, col = map(int,input().split());
for _ in range(row):
  tmpList = list(map(int,list(input())));
  table.append(tmpList);

#=== 풀이 ===#

#startPoint 선택
for i in range(row):
  for j in range(col):
    #초기화
    selectedNum = []; #selectedNum 초기화;
    
    
    startPoint = [i,j];
    selectedNum.append(table[i][j]); #selectedNum배열에 추가

    #secondPoint 선택
    for p in range(row):
      for q in range(col):
        diff = []; #diff 초기화
        tmpList = [];

        if p == i and q == j: continue; #같은 칸은 피해야지.
        secondPoint = [p,q];
        tmpList.append(table[p][q]); #selectedNum배열에 추가
        diff = [p-i, q-j]; #등차 결정.

        otherPoint = secondPoint;
        #otherPoint 선택
        while(1):
          y = otherPoint[0] + diff[0];
          x = otherPoint[1] + diff[1];
          if y < 0 or y >= row or x >= col or x < 0: break; #범위 넘어가면 루프 탈출

          otherPoint = [y,x];
          print(y,x);
          tmpList.append(table[y][x]); #selectedNum배열에 추가

        selectedNum += tmpList;
        print(selectedNum);
        # if isSquareNum(num):
        #   if num > max_squareNum:
        #     max_squareNum = num;


print(max_squareNum);
        


        














