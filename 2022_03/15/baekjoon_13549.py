#baekjoon_13549_숨바꼭질3

#baekjoon_12581_숨바꼭질
from collections import deque

def BFS(N,K):
    queue = deque();
    queue.append([N,0]);

    visited = [100001 for _ in range(100001)];

    while queue:
        pos, time = queue.popleft();
        #print(pos,time);
        if pos > 100000: #범위에서 벗어남
            continue;

        if visited[pos] <= time: #더 좋은 경우가 이미 존재
            continue;
        visited[pos] = time;

        if pos == K: #목표 지점 도달
            break;

        #걷기 + 1
        if pos < K:
            queue.append([pos+1, time+1]);
        #걷기 -1
        if pos > 0:
            queue.append([pos-1, time+1]);
        #순간이동
        if pos < K:
            queue.appendleft([pos * 2, time]);


    return visited[K];






N , K = map(int,input().split()) # 수빈이의 위치, 동생의 위치

if K <= N:
    result = N - K;
else:
    result = BFS(N,K);

print(result);
