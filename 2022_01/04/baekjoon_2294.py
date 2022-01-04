#baekjoon_2294_동전 2

#=== import module ===#
from collections import deque
#=== variable declare ===#
n = -1; #동전의 가짓수
k = -1; #목표 합
coins = []; #동전 값 배열
dp = []; #dp 배열
#=== Function define ===#
def BFS(k):
  queue = deque();
  for price in coins:
    if price <= k:
      queue.append(price);
  find = False;
  while queue:
    for _ in range(len(queue)):
      curPrice = queue.popleft();
      for addPrice in coins:
        nextPrice = curPrice + addPrice;
        if nextPrice > k : continue; #목표 합계 넘음
        if dp[nextPrice] != None: continue; #이미 방문했던 값
        queue.append(nextPrice); #queue에 추가
        dp[nextPrice] = dp[curPrice] + 1; #dp 배열에 값 입력

        if nextPrice == k: find = True; break; #목표 값 도착
      
      if find: break;
    if find: break;
  
  if not find: return -1;
  else: return dp[k];



      

    




#=== main function ===#
n,k = map(int,input().split());


for _ in range(n):
  coins.append(int(input()));

coins = list(set(coins)); #중복 동전 제거
coins.sort(); #코인 오름차순 정리
n = len(coins);

#dp 초기값 설정
dp = [None for _ in range(k+1)];
for price in coins:
  if price <= k:
    dp[price] = 1;

print(BFS(k));


