#baekjoon_2206_벽부수고 이동하기
import collections

N,K = map(int,input().split());

Map = [[-1 for _ in range(K+2)] for _ in range(N+2)];

for i in range(1,N+1):
    inputData = list(map(int,list(input())));
    for j in range(1,K+1):
        Map[i][j] = inputData[j-1];

def BFS(N,K):

    queue = collections.deque();
    queue.append([1,1,1]); # y좌표, x좌표, 벽 부수기 가능 여부
    visited = [[[False for _ in range(2)] for _ in range(K+1)] for _ in range(N+1)];
    dx = [-1,1,0,0]; dy = [0,0,-1,1];

    action = 1;
    success = False;
    while queue:

        for _ in range(len(queue)):
            y,x,k = queue.popleft();

            if y == N and x == K: #목표 지점 도달
                queue.clear();
                success = True;
                break;

            if visited[y][x][k] or visited[y][x][1]: continue; #이미 해당 지점을 방문한 경우

            visited[y][x][k] = True;

            # 벽 부수기 X
            for i in range(4):
                ny = y + dy[i]; nx = x + dx[i];
                if Map[ny][nx] == -1: continue; #Map을 벗어난 경우
                if Map[ny][nx] == 1: continue; #해당 지점에 벽이 있는 경우
                queue.append([ny,nx,k]);
            # 벽 부수고 이동 O
            if k != 0:
                for i in range(4):
                    ny = y + dy[i]; nx = x + dx[i];
                    if Map[ny][nx] == -1: continue;  # Map을 벗어난 경우
                    if Map[ny][nx] == 1:  # 해당 지점에 벽이 있는 경우
                        queue.append([ny, nx, k-1]);

        action += 1;

    if success:
        return action -1;
    else:
        return -1;






print(BFS(N,K));






