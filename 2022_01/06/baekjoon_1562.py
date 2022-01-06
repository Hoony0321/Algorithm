#baekjoon_1562_계단 수

#=== import module ===#

#=== variable declare ===#
N = -1; #목표 자릿수
dp = []; #dp 배열
#=== Function define ===#
def FindStepNum(N):
  length = 1;
  result = 0;
  while(length < N):
    for endNum in range(10):
      for visited in range(0,(1 << 10)):
        if dp[length][endNum][visited] == 0: continue; #해당하는 경우 존재하지 않음.
        if endNum == 0: 
          dp[length + 1][1][visited | (1 << 1)] += dp[length][endNum][visited];
        elif endNum == 9:
          dp[length + 1][8][visited | (1 << 8)] += dp[length][endNum][visited];
        else: 
          dp[length + 1][endNum-1][visited | (1 << (endNum-1))] += dp[length][endNum][visited];
          dp[length + 1][endNum+1][visited | (1 << (endNum+1))] += dp[length][endNum][visited];
    length += 1;

  for endNum in range(10):
    result += dp[N][endNum][(1 << 10) - 1];
  
  return result;
  
  
  

#=== main function ===#
N = int(input());

dp = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(N+1)];

for i in range(10):
  dp[1][i][1 << i] = 1;
dp[1][0][1] = 0; #맨 첫자리는 0이 올수 없음. 향후 다시 처리해보자.

print(FindStepNum(N) % 1000000000);