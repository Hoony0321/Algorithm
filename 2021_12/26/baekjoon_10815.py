#baekjoon_10815_숫자 카드

#=== import module ===#
import math
#=== variable declare ===#

#=== Function define ===#

#=== main function ===#
N = int(input());
N_array = list(map(int,input().split()));
M = int(input());
M_array = list(map(int,input().split()));
N_array.sort(); #오름 차순 정렬

for target in M_array:
  startIdx = 0;
  endIdx = N-1;
  search = False;
  while(1):
    
    if startIdx > endIdx : break;

    midIdx = math.floor((endIdx + startIdx)/2);
    if N_array[midIdx] == target: #타겟인 경우 -> 탐색 종료
      search = True; break;

    elif N_array[midIdx] < target: #타겟이 더 큰 경우 -> 오른쪽으로 탐색
      startIdx = midIdx + 1;

    elif N_array[midIdx] > target: #타겟이 더 작은 경우 -> 왼쪽으로 탐색
      endIdx = midIdx - 1;
  
  if search: print(1, end=' ');
  else: print(0, end=' ');


  