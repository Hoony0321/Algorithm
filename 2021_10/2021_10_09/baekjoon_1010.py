#baekjoon_1010_다리놓기

factorial_dp = [0 for i in range(32)];
factorial_dp[0]=1; factorial_dp[1]=1; factorial_dp[2]=2;

def combinations(N,R):
  top = factorial(N);
  bottom = factorial(R) * factorial(N-R);
  return int(top/bottom);

def factorial(N):
  if(factorial_dp[N] != 0):
    return factorial_dp[N];

  factorial_dp[N] = N * factorial(N-1);
  return factorial_dp[N];


testCase = int(input());

for tCase in range(testCase):
  N,M = map(int,(input().split()));
  result = combinations(M,N);
  print(result);