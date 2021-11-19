#baekjoon_1051_숫자 정사각형 (수학문제)

#=== import module ===#

#=== Function define ===#
def checkIsAvailable(row,col,size,N,M):
  rightEnd = col + size -1;
  bottomEnd = row + size - 1;

  if bottomEnd >= N : #아랫부분 범위 초과
    return -1;
  elif rightEnd >= N : #오른쪽부분 범위 초과
    return 0;
  else: #범위 안에 있음.
    return 1;

def checkConerValue(row,col,size,rect):
  val = rect[row][col];

  #우측 하단
  if rect[row + size -1][col + size - 1] != val:
    return False;
  #좌측 하단
  elif rect[row + size -1][col] != val:
    return False;
  #우측 상단
  elif rect[row][col + size -1] != val:
    return False;
  else:
    return True;


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

while(not found):
  row = -1;
  col = -1;
  while(row != None): #row증가
    row += 1;
    while(col != None): #col증가
      col += 1;
      print("row : {}, col : {}".format(row,col));
      checkVariable = checkIsAvailable(row,col,size,N,M);
      if checkVariable == -1: #아예 나가야 함.
        row = None;
        col = None;
      elif checkVariable == 0: #다음 줄로 넘어가야 함.
        col = None;
      elif checkVariable == 1: #가능함. ->  다음 칸으로 진행
        if checkConerValue(row,col,size,rect): #코너 값 같음
          found = True;
          col = None; #반복문 탈출
          row = None;
        else: #코너 값 다름
          pass;

  size -= 1;
        

print(size);

