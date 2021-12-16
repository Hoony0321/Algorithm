#baekjoon_16236_아기 상어

#=== import module ===#
from collections import deque
from copy import deepcopy
#=== variable declare ===#
matrix = []; fishList = []; curPos = [-1,-1];
#=== Function define ===#
def findFish(N):
  fishList = [];
  for i in range(N):
    for j in range(N):
      elem = matrix[i][j];
      if elem != 0:
        if elem == 9: curPos = [i,j];
        else fishList.append([i,j,elem]); # y,x,size

def solve(N):
  curTime = 0;
  curSize = 2;
  targetFishList = [];
  findFish(N);
  needMom = True;

  for fish in fishList:
    if fish[2] < curSize:
      needMom = False;
      targetFishList.append(deepcopy(fish));

  if needMom: return curTime;

  BFS(curPos,curSize,)






#=== main function ===#
N = int(input());
for _ in range(N):
  matrix.append(list(map(int,input().split())));

solve(N);