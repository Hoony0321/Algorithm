#baekjoon_9465_스티커

#=== import module ===#

#=== variable declare ===#
n = -1; #스티커의 열 개수
stickers = []; #스티커 값 배열
#=== Function define ===#
def ReturnMaxVal(n):
  dp = [[0 for _ in range(n)] for _ in range(2)];

  if n == 1:
    return max(stickers[0][0], stickers[1][0]);
  
  dp[0][0] = stickers[0][0]; dp[1][0] = stickers[1][0];
  dp[0][1] = stickers[1][0] + stickers[0][1]; dp[1][1] = stickers[0][0] + stickers[1][1];

  if n == 2:
    return max(dp[0][1], dp[1][1]);
  
  for i in range(2,n):
    value = stickers[0][i];
    dp[0][i] = max(dp[1][i-1] + value, dp[0][i-2] + value, dp[1][i-2] + value);
    value = stickers[1][i];
    dp[1][i] = max(dp[0][i-1] + value, dp[0][i-2] + value, dp[1][i-2] + value);
  
  return max(dp[0][n-1] , dp[1][n-1]);

#=== main function ===#
testCase = int(input());

for _ in range(testCase):
  stickers = [];
  n = int(input());
  for _ in range(2):
    stickers.append(list(map(int,input().split())));
  
  print(ReturnMaxVal(n));