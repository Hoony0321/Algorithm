#baekjoon_17143_낚시왕

#=== import module ===#

#=== variable declare ===#
R = -1; #열 개수
C = -1; #행 개수
M = -1; #상어의 수
board = []; #맵 행렬
sharkArr = [None for _ in range(10001)]; #상어 정보 배열 (크기로 구분 *크기 최대 10000)
sharkIdx = []; #살아있는 상어한테 빠른 접근을 위한 인덱스 배열
dyx = [None , [-1,0], [1,0], [0,1], [0,-1]] #상 우 하 좌 (0번 인덱스는 사용 안 함)

#=== Function define ===#
def TurnDirection(d):
  if d == 1:
    return 2;
  elif d == 2:
    return 1;
  elif d == 3:
    return 4;
  else: return 3;

def MoveShark(size,be_eaten_shark_size):
  global R,C;
  y,x,s,d = sharkArr[size];
  ny = y; nx = x;

  if d <= 2: s %= (R-1) * 2;
  else: s %= (C-1) * 2;

  remain_speed = s;
  while remain_speed > 0:
    if d == 1:
      dy = min(ny - 1, remain_speed);
      ny -= dy;
      remain_speed -= dy;
    elif d == 2:
      dy = min(R - ny, remain_speed); # 갈 수 있는 거리, 남은 속도
      ny += dy;
      remain_speed -= dy;
    elif d == 3:
      dx = min(C - nx, remain_speed); # 갈 수 있는 거리, 남은 속도
      nx += dx;
      remain_speed -= dx;
    else:
      dx = min(nx - 1, remain_speed); # 갈 수 있는 거리, 남은 속도
      nx -= dx;
      remain_speed -= dx;

    if d <= 2: 
      if ny == 1 or ny == R:
        d = TurnDirection(d);
    else:
      if nx == 1 or nx == C :
        d = TurnDirection(d);
  
  if board[ny][nx] != 0:
    #해당 칸에 상어 존재 -> 사이즈가 작은 상어부터 큰 물고기 순으로 이동하므로 해당 칸에 이미 있는 상어는 현 상어보다 작은 상어.
    be_eaten_shark_size.append(board[ny][nx]);

  board[ny][nx] = size;
  sharkArr[size] = [ny,nx,s,d];

  
  
      


def Fishing(R,C):
  global board;
  sharkIdx.sort(); #오름 차순 정렬
  fishmenCol = 1; #1에서 최대 C까지 이동
  getWeight = 0; #잡은 상어 무게 합.
  while(fishmenCol <= C):
    # 1.해당 열에서 땅에 가장 가까운 상어 포획
    for row in range(1,R+1): #1부터 R까지 진행
      if board[row][fishmenCol] != 0: #상어 존재 -> 포획
        sharkIdx.remove(board[row][fishmenCol]); # 상어 인덱스 삭제
        getWeight += board[row][fishmenCol];
        board[row][fishmenCol] = 0;
        break;
    
    # 2.상어 이동
    board = [[0 for _ in range(C+1)] for _ in range(R+1)]; #이동하기 전 보드 초기화.
    be_eaten_shark_size = [];
    for size in sharkIdx:
      MoveShark(size,be_eaten_shark_size);
    
    # 3. 먹힌 상어 sharkIdx에서 제거
    for shark in be_eaten_shark_size:
      sharkIdx.remove(shark);
    
    fishmenCol += 1;
  
  return getWeight;



#=== main function ===#
R,C,M = map(int,input().split());
board = [[0 for _ in range(C+1)] for _ in range(R+1)];

for _ in range(M):
  r,c,s,d,z = map(int,input().split());

  if board[r][c] != 0 and z < board[r][c]: #이미 해당 위치에 존재하는 상어 존재
    continue; #자신보다 큰 상어이므로 잡아먹힘 -> 건너뜀.
  
  board[r][c] = z;
  sharkIdx.append(z);
  sharkArr[z] = [r,c,s,d];

print(Fishing(R,C));



