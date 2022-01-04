#baekjoon_9461_파도반 수열

#=== import module ===#

#=== variable declare ===#
N = -1; #찾고자 하는 순서의 수.
dp = [None for _ in range(100)]; #dp 배열

#=== Function define ===#
def solve(N):
  
  for i in range(3,N):
    if dp[i] != None:
      continue;
    dp[i] = dp[i-3] + dp[i-2];
  
  return dp[N-1];


#=== main function ===#
testCase = int(input());
dp[0] = 1; dp[1] = 1; dp[2] = 1; #처음 dp set, 0,1,2번째는 공식 통용되지 않음.
for _ in range(testCase):
  N = int(input());
  print(solve(N));
