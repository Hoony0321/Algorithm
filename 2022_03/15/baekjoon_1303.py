#baekjoon_1303_전투
import collections

N,M = map(int,input().split());

map = [None for _ in range(M)];

for i in range(M):
    map[i] = list(input());

def BFS(x,y,visited):
    global N,M;
    queue = collections.deque();
    queue.append([x,y]);
    target = map[y][x];

    count = 0;
    dx = [-1,1,0,0]; dy = [0,0,-1,1];
    while queue:
        x,y = queue.popleft();

        if visited[y][x]: #이미 방문한 곳
            continue;
        visited[y][x] = True;
        count += 1;

        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i];

            if not (0 <= nx < N and 0 <= ny < M): #범위에서 벗어남.
                continue;

            if map[ny][nx] != target: #타겟이 아님.
                continue;

            queue.append([nx,ny]);

    return count;

visited = [[False for _ in range(N)] for _ in range(M)];

power = {'W' : 0 , 'B' : 0};

for i in range(N):
    for j in range(M):
        if visited[i][j]: continue;
        result = BFS(i,j,visited);
        power[map[i][j]] += result ** 2;


print(power['W'], power['B']);







