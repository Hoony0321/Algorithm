#baekjoon_1052_물병

#=== import module ===#

#=== Function define ===#

#=== variable declare ===#
K = 0; N = 0; buyBottle = 0;

#=== main function ===#
N,K = map(int,input().split());

if N <= K:
  print(0);
  exit(0);

while(1):
  cnt = 0;
  tmpN = N + buyBottle;
  while(tmpN > 0):
    if(tmpN%2):
      cnt += 1;
    tmpN = int(tmpN/2);
  
  if cnt <= K:
    break;
  else:
    buyBottle += 1;

print(buyBottle);
    
      






