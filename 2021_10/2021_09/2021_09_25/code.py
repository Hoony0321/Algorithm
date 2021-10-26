dp = [None, None] * 100;
dp[0] = [1,0];
dp[1] = [0,1];

testCase = int(input());

def solve(n):
  if dp[n] is None:
    dp[n] = [solve(n-1)[0] + solve(n-2)[0] , solve(n-1)[1] + solve(n-2)[1]];
  return dp[n];

for i in range(testCase):
  testNum = int(input());
  result = solve(testNum);
  print(result[0] , result[1]);