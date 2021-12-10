#baekjoon_23757_2021고려대학교 프로그래밍 경시대회

#=== import module ===#
import heapq
import sys

input = sys.stdin.readline
#=== variable declare ===#

#=== Function define ===#

#=== main function ===#
N,M = map(int,input().split());
presents = list(map(int,input().split())); 
wishNum = list(map(int,input().split()));

q = [];
for elem in presents:
  heapq.heappush(q,-elem);

disappoint = False;
for idx in range(M):
  max_present = -heapq.heappop(q);
  
  if max_present < wishNum[idx]:
    disappoint = True; break;
  else:
    max_present -= wishNum[idx];
    heapq.heappush(q,-max_present);

if not disappoint: print(1);
else: print(0);