#baekjoon_1027_고층 건물

def maxVisibleBuilding():
  max = 0;
  for i in range(num_building):
    visible = ReturnNumVisible(i);
    if max < visible:
      max = visible;
    
  return max;

#i가 작고 j가 더 큼
def isVisible(i,j):
  if dp[i][j] == -1: #dp값 설정 
    target_slope = getSlope(i,j);
    index = i+1;
    isAvailable = True;
    while(index < j):
      x = index - i;
      limitHeight = target_slope * x + buildings[i];
      if limitHeight <= buildings[index]:
        isAvailable = False;
        break;
      index += 1;
    if isAvailable: 
      dp[i][j] = 1; dp[j][i] = 1;
    else:
      dp[i][j] = 0; dp[j][i] = 0;
  
  return dp[i][j];
    

# i < j
def getSlope(i,j):
  dx = i - j;
  dy = buildings[i] - buildings[j];
  return dy/dx;


  

def ReturnNumVisible(num):
  cnt = 0;
  for i in range(num_building):
    if i == num: continue;
    if isVisible(num,i): cnt += 1;
  return cnt;


#MAIN
num_building = int(input());
buildings = list(map(int,input().split()));
dp = [[-1 for i in range(num_building)] for j in range(num_building)];




print(maxVisibleBuilding());
