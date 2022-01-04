#baekjoon_2294_동전 2

#=== import module ===#

#=== variable declare ===#
n = -1; #동전의 가짓수
k = -1; #목표 합
coins = []; #동전 값 배열
#=== Function define ===#
def greedy(n,k):
  count = 0;
  remain = k;
  startPoint = n-1;
  while(1):
    print(remain);
    if remain == 0: #성공 종료 조건
      available = 1; break;

    useCoin = -1;
    
    for i in range(startPoint,-1,-1): #startPint부터 0까지 반복
      if coins[i] <= remain:
        useCoin = i;  startPoint = i;
        remain -= coins[useCoin];
        count += 1;
        break;
    
    if useCoin == -1: #사용 가능한 동전 존재하지 않음.
      available = -1; break;
  
  if available == 1:
    return count;
  else:
    return -1;

    




#=== main function ===#
n,k = map(int,input().split());

for _ in range(n):
  coins.append(int(input()));
  
coins = list(set(coins)); #중복 동전 제거
coins.sort(); #코인 오름차순 정리


print(greedy(n,k));

