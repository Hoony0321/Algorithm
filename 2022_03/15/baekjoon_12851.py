#baekjoon_12581_숨바꼭질
from collections import deque

def BFS(N,K):
    queue = deque();
    queue.append(N);

    time = 0;
    count = 0;
    find = False;

    visited = [100001 for _ in range(100001)];
    while queue and not find:

        for _ in range(len(queue)):
            pos1 = queue.popleft();

            if pos1 > 100000:
                continue; #범위에서 벗어남.

            if pos1 == K: #동생 찾음.
                count += 1;
                find = True;

            if visited[pos1] < time: #가지치기
                continue;
            else:
                visited[pos1] = time;


            if not find: #아직 동생 못 찾음.
                #+1
                if pos1 < K:
                    queue.append(pos1 +1);
                #-1
                if pos1 > 0:
                    queue.append(pos1 -1);
                #*2
                if pos1 < K:
                    queue.append(pos1 * 2);

        time += 1;

    return [time -1,count];





N , K = map(int,input().split()) # 수빈이의 위치, 동생의 위치

if K <= N:
    result = [N - K , 1];
else:
    result = BFS(N,K);

print(result[0]);
print(result[1]);