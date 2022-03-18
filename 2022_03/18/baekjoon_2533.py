#baekjoon_2533_사회망 서비스

def DFS(curNode):
    #print(curNode);
    dp[curNode][1] = 1;
    visited[curNode] = True;
    for nextNode in Tree[curNode]:
        if not visited[nextNode]:
            DFS(nextNode);
            dp[curNode][0] += dp[nextNode][1];
            dp[curNode][1] += min(dp[nextNode][1], dp[nextNode][0]);

N = int(input()); #정점 개수

Tree = [[] for _ in range(N+1)];

for _ in range(N-1):
    fromNode, toNode = map(int,input().split());
    Tree[fromNode].append(toNode);
    Tree[toNode].append(fromNode);

dp = [[0 for _ in range(2)] for _ in range(N+1)];

visited = [False for _ in range(N+1)];
DFS(1);

print(min(dp[1][0], dp[1][1]))



