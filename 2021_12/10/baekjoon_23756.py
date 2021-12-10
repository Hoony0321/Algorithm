#baekjoon_23756_노브 돌리기_2021고려대학교 프로그래밍 경시대회

#=== import module ===#

#=== variable declare ===#
N = 0; A = []; sum = 0;
#=== Function define ===#

#=== main function ===#
N = int(input());
for _ in range(N+1):
  A.append(int(input()));

start = 0;

while(start < N):
  fromA = A[start];
  toA = A[start+1];

  diff = abs(fromA - toA);

  if diff > 180:
    if fromA > toA: fromA = 360 - fromA;
    else: toA = 360 - toA;
    diff = fromA + toA;
  
  sum += diff;
  start += 1;

print(sum);
    
