#baekjoon_23758_중앙값제거_2021고려대학교 프로그래밍 경시대회

#=== import module ===#
import math
import sys
import heapq

input = sys.stdin.readline
#=== variable declare ===#

#=== Function define ===#

#=== main function ===#
N = int(input());
S = list(map(int,input().split()));
S.sort();
center = math.floor((N+1)/2);

sum = 0;
for i in range(center):
  sum += int(math.log(S[i],2));

print(sum + 1);