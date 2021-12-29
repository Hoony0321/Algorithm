#baekjoon_1072_게임

#=== import module ===#

#=== variable declare ===#

#=== Function define ===#

#=== main function ===#
x,y = map(int,input().split()); #게임 횟수, 이긴 횟수
currentRate = y*100 // x;
if currentRate >= 99: print(-1); exit(0);

high = 1000000000;
row = 0;
result = -1;
while(row <= high):

  mid = (high + row) // 2;
  rate = (y + mid) * 100 // (x + mid);

  if currentRate >= rate:
    row = mid + 1;
    result = mid + 1;
  else:
    high = mid - 1;
    



print(result);