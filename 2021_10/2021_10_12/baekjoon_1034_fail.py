#baekjoon_1034_램프
from copy import copy

def SwitchingRamp(ramp_map,column):
  for j in range(row):
    state = ramp_map[j][column];
    ramp_map[j][column] = 1 if state == 0 else 0;

def ReturnTurnOnRampRow(map):
  cnt = 0;
  for item in map:
    isTurnOnRow = True;
    for val in item:
      if val == 0: 
        isTurnOnRow = False;
        break;
    if isTurnOnRow: cnt += 1;
  return cnt;
  
def FindingMax(stage,map):
  if stage > num_switch:
    global maxVal;
    result = ReturnTurnOnRampRow(map);
    if maxVal < result : maxVal = result;
  else:
    for i in range(col):
      tmp_map = copy(map);
      SwitchingRamp(tmp_map,i);
      FindingMax(stage+1,tmp_map);


row,col = map(int,(input().split()));

ramp_map = [[0 for i in range(col)] for j in range(row)];

for i in range(row):
  ramp_map[i] = list(map(int,list(input())));

num_switch = int(input());

maxVal = 0;
FindingMax(1,copy(ramp_map));
print(maxVal);
