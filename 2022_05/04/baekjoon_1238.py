# 문제 정보 baekjoon_1238 파티

# === import module ===#
import heapq
# === variable declare ===#

# === Function define ===#
def dijkstra(start):
    global N,X

    V = [ i for i in range(1,N+1)];
    Y = [];

    length = [None for _ in range(N+1)]; #start부터 i까지 거리
    touch = [start for _ in range(N+1)]; #start가 제일 가까운 정점으로 다 세팅

    edges = set();


    for i in range(1, N+1): #1부터 N까지
        length[i] = W[start][i];

    for _ in range(N): #N-1회 반복
        min = float('INF');
        vnear = -1;
        for vertex in range(1,N+1): #1부터 N까지 반복
            if(min > length[vertex]):
                min = length[vertex];
                vnear = vertex;

        edges.add([touch[vnear], vnear]);




# === main function ===#
N,M,X = map(int(input().split()));
W = [[float('INF') for _ in range(N+1)] for _ in range(N+1)];

for _ in range(M):
    fromV,toV,weight = map(int,input().split());
    W[fromV][toV] = weight;




