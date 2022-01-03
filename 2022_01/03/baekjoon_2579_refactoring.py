#baekjoon_2579_계단 오르기_dp 순서 있을 때

#=== import module ===#

#=== variable declare ===#
N = None; #계단 개수
stairs = [0]; #계단 정보
dp = []; #dp 배열
#=== Function define ===#
def UpStair(N):
  if N < 2:
    return stairs[N];
  elif N == 2:
    return stairs[1] + stairs[2];

  #dp[i] = max( dp[i-2] + stairs[i] , dp[i-3] + stairs[i-1] + stairs[i] );
  dp[0] = 0; dp[1] = stairs[1]; dp[2] = stairs[1] + stairs[2];

  for i in range(3,N+1):
    dp[i] = max( dp[i-2] + stairs[i] , dp[i-3] + stairs[i-1] + stairs[i] );
  
  return dp[N];

  
  

#=== main function ===#
N = int(input());
dp = [None for _ in range(N+1)];
for _ in range(N):
  stairs.append(int(input()));

print(UpStair(N));

