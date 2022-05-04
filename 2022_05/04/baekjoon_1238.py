# 문제 정보 baekjoon_1238 파티

# === import module ===#
import heapq
# === variable declare ===#

# === Function define ===#
def dijkstra(start):
    global N,X

    V = [ i for i in range(1,N+1)];
    Y = [];

    length = [ None for i in range(N+1)]; #start부터 i까지 거리
    vnear = -1;
    for i in range(1, N+1): #1부터 N까지
        length[i] = W[start][i];

    for _ in range(N): #N-1회 반복




# === main function ===#
N,M,X = map(int(input().split()));
W = [[float('INF') for _ in range(N+1)] for _ in range(N+1)];

for _ in range(M):
    fromV,toV,weight = map(int,input().split());
    W[fromV][toV] = weight;




