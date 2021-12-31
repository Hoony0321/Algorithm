#baekjoon_1063_킹

#=== import module ===#

#=== variable declare ===#
nxy = [(0,1), (0,-1), (-1,0), (1,0), (1,1), (1,-1), (-1,1), (-1,-1)];
#=== Function define ===#
def MovingKing(move):
  global king_pos,stone_pos;
  moveNum = -1;
  if move == 'R':
    moveNum = 0;
  elif move == 'L':
    moveNum = 1;
  elif move == 'B':
    moveNum = 2;
  elif move == 'T':
    moveNum = 3;
  elif move == 'RT':
    moveNum = 4;
  elif move == 'LT':
    moveNum = 5;
  elif move == 'RB':
    moveNum = 6;
  elif move == 'LB':
    moveNum = 7;

  next_king_pos = [king_pos[0] + nxy[moveNum][0] , king_pos[1] + nxy[moveNum][1]];
  if not(1 <= next_king_pos[0] <= 8 and 1 <= next_king_pos[1] <= 8): return; #체스가 밖으로 나감
  if next_king_pos[0] == stone_pos[0] and next_king_pos[1] == stone_pos[1]: #체스 다음 위치가 돌일 경우
    next_stone_pos = [stone_pos[0] + nxy[moveNum][0] , stone_pos[1] + nxy[moveNum][1]];
    if not(1 <= next_stone_pos[0] <= 8 and 1 <= next_stone_pos[1] <= 8): return; #돌이 밖으로 나감
    stone_pos = next_stone_pos;
  king_pos = next_king_pos;


def PosTransformToValue(pos_char): #return row, col
  return [int(pos_char[1]), ord(pos_char[0]) - 64];

def PosTransformToChar(pos_value): #return col,row
  return chr(pos_value[1] + 64) + str(pos_value[0]);
#=== main function ===#
king_pos, stone_pos, num = input().split();

stone_pos = PosTransformToValue(stone_pos);
king_pos = PosTransformToValue(king_pos);

for _ in range(int(num)):
  move = input();
  MovingKing(move);

  

print(PosTransformToChar(king_pos));
print(PosTransformToChar(stone_pos));

  