#baekjoon_1007_벡터매칭

#=== import module ===#
import math
import itertools
#=== variable declare ===#
pointArr = []; #점 배열
dp = []; #dp배열
min_dist = float('INF'); #최소거리
#=== Function define ===#
def ReturnDist(arrA):
  dx = 0; dy = 0;#baekjoon_1007_벡터매칭

#=== import module ===#
import math
import itertools
#=== variable declare ===#
pointArr = []; #점 배열
dp = []; #dp배열
min_dist = float('INF'); #최소거리
#=== Function define ===#
def ReturnDist(arrA):
  dx = 0; dy = 0;
  for i in range(N):
    if i in arrA: #더하는 쪽
      dx += pointArr[i][0];
      dy += pointArr[i][1];
    else: #빼는 쪽
      dx -= pointArr[i][0];
      dy -= pointArr[i][1];
  
  return (dx ** 2 + dy ** 2) ** 0.5;
#=== main function ===#
T = int(input());

for _ in range(T):
  N = int(input()); #점의 개수
  pointArr = [];
  dp = [[None for _ in range(N)] for _ in range(N)];
  min_dist = float('INF');
  for _ in range(N):
    x,y = map(int,input().split());
    pointArr.append((x,y));
  

  combList = list(itertools.combinations([i for i in range(N)],N//2));  
  

  for arrA in combList:
    dist = ReturnDist(arrA);
    min_dist = min(min_dist,dist);
  
  print(min_dist);
  
  


  for i in range(N):
    if i in arrA: #더하는 쪽
      dx += pointArr[i][0];
      dy += pointArr[i][1];
    else: #빼는 쪽
      dx -= pointArr[i][0];
      dy -= pointArr[i][1];
  
  return (dx ** 2 + dy ** 2) ** 0.5;
#=== main function ===#
T = int(input());

for _ in range(T):
  N = int(input()); #점의 개수
  pointArr = [];
  dp = [[None for _ in range(N)] for _ in range(N)];
  min_dist = float('INF');
  for _ in range(N):
    x,y = map(int,input().split());
    pointArr.append((x,y));
  

  combList = list(itertools.combinations([i for i in range(N)],N//2));  
  

  for arrA in combList:
    dist = ReturnDist(arrA);
    min_dist = min(min_dist,dist);
  
  print(min_dist);
  
  

