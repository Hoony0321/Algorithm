#baekjoon_1033_칵테일

def gcd(a, b):  #최대공약수 구하기

    tmpB = 0;
    while (b != 0):
        tmpB = b;
        b = a % b;
        a = tmpB

    return tmpB;

def DFS(index, visited):
    global N;

    if visited[index]: #이미 방문한 곳
        return;
    visited[index] = True;

    for relation in graph[index]:
        vertex, ratio = relation;

        multiple = mass[index] // ratio[0];

        if mass[vertex] == ratio[1] * multiple: #비율이 맞는 상태.
            return;
        else: #비율이 안 맞는 상태. - update 진행
            mass[vertex] ==
            DFS(vertex, [False for _ in range(N)]);



N = int(input()); #재료 개수

mass = [[] for _ in range(N)];
graph = [[] for _ in range(N)];
for _ in range(N):
    a,b,p,q = map(int,input().split());

    gcdVal = gcd(p, q); _p = p // gcdVal; _q = q // gcdVal; #비율 조정
    graph[a].append([b,(_p,_q)]);
    graph[b].append([a, (_q, _p)])

    mass[a].append(_p);
    mass[b].append(_q);

visited = [False for _ in range(N)];













