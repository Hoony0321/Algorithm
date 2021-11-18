#baekjoon_1051_숫자 정사각형 (수학문제)

#=== import module ===#

#=== Function define ===#

#=== variable declare ===#

#=== main function ===#

N,M = map(int,input().split());
rect = [];

for _ in range(N):
  tmpList = list(map(int,list(input())));
  rect.append(tmpList);

size = min(N,M);
point = [0,0];
found = False;
while(1):
  row = 0;
  col = 0;
  while(!found): #row증가
    while(col != -1): #col증가
      checkVariable = checkIsAvailable(row,col,size,rect);
      if checkVariable == -1: #아예 나가야 함.
        row = -1;
        col = -1;
      elif checkVariable == 0: #다음 줄로 넘어가야 함.
        col = -1;
      elif checkVariable == 1: #가능함. ->  다음 칸으로 진행
        pass; #각 꼭짓점 확인해야함.
  
    if row == -1: #아예 탈출해야 함.
      pass;
    else:
      row += 1; #다음 줄로 진행

