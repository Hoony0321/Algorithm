#baekjoon_13913_숨바꼭질4

#baekjoon_12581_숨바꼭질
from collections import deque

def BFS(N,K):
    queue = deque();
    queue.append([N , [N]]); #현재 위치, 거쳐간 곳 표현

    time = 0;
    found = False;
    result = [];
    visited = [100001 for _ in range(100001)];
    while queue and not found:

        for _ in range(len(queue)):
            pos, route = queue.popleft();

            if pos > 100000:
                continue; #범위에서 벗어남.

            if pos == K: #동생 찾음.
                found = True;
                result = [time, route];
                break;

            if visited[pos] < time: #가지치기
                continue;
            else:
                visited[pos] = time;


            if not found: #아직 동생 못 찾음.
                #+1
                if pos < K:
                    queue.append([pos + 1, route + [pos + 1]]);
                #-1
                if pos > 0:
                    queue.append([pos - 1, route + [pos - 1]]);
                #*2
                if pos < K:
                    queue.append([pos * 2, route + [pos * 2]]);

        time += 1;

    return result




N , K = map(int,input().split()) # 수빈이의 위치, 동생의 위치

if K <= N:
    result = [N - K , [i for i in range(N,K-1,-1)]];
else:
    result = BFS(N,K);

print(result[0]);
for elem in result[1]:
    print(elem,end=' ');
