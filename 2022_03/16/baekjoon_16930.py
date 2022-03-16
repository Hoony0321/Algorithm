#baekjoon_16930_달리기
from collections import deque
import sys
input = sys.stdin.readline

def BFS(N,M,K,curPos,destPos):
    queue = deque();
    queue.append(curPos);
    visited = [[-1 for _ in range(M+1)] for _ in range(N+1)]
    visited[curPos[0]][curPos[1]] = 0;

    arrive = False;
    time = 0;

    dx = [1,-1,0,0]; dy = [0,0,1,-1]; delta = [i for i in range(1,K+1)];
    while queue and not arrive:

        for _ in range(len(queue)):
            curPos = queue.popleft();

            if curPos == destPos:  # 도착
                arrive = True;
                break;

            for i in range(4):
                for mulNum in delta:
                    ny = curPos[0] + dy[i] * mulNum; nx = curPos[1] + dx[i] * mulNum;
                    if ny < 1 or ny > N or nx < 1 or nx > M: break; #맵에서 벗어남.
                    if mapInfo[ny][nx] == '#': #해당 지점이 벽임. - 같은 방향으로 계속 진행해도 이미 벽에 가로 막힘.
                        break;
                    if visited[ny][nx] == -1:
                        queue.append([ny,nx]);
                        visited[ny][nx] = time +1;
                    elif visited[ny][nx] == time +1: continue;
                    else: break;

                    # if visited[ny][nx] != -1: continue; #이미 방문한 지점임.
                    #
                    # #queue에 추가
                    # queue.append([ny,nx]);
                    # visited[ny][nx] = time+1;


        if not arrive: time += 1;

    return visited[destPos[0]][destPos[1]];





N,M,K = map(int,input().split()); #세로, 가로, 최대 가능 이동

mapInfo = [[None for _ in range(M+1)] for _ in range(N+1)]

for i in range(1,N+1):
    info = list(input());
    for j in range(1,M+1):
        mapInfo[i][j] = info[j-1];

y1,x1,y2,x2 = map(int,input().split());

curPos = [y1,x1];
destPos = [y2,x2];

print(BFS(N,M,K,curPos,destPos));