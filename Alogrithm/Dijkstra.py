#다익스트라 알고리즘
#방향/가중치 있는 그래프에서 특정 노드 위치에서 각 노드 최단경로 찾기

def dijkstra(start):
    global N

    V = [ i for i in range(1,N+1)]; #모든 Node 번호 array
    Y = [start]; #selected 된 Node 번호 array
    NoC = 0; #length 업데이트하는 최대 횟수
    edgeToVStart = 0; #vStart과 연결된 엣지 수

    length = [None for _ in range(N+1)]; #start부터 i까지 거리 array
    touch = [start for _ in range(N+1)]; #distance[vertex] 에서 붙어있는 Node 번호 array
    save_length = [None for _ in range(N)]; #실제 거리

    edges = []; # 선택된 edge array

    for i in range(1, N+1): #1부터 N까지
        length[i] = W[start][i];
        touch[i] = 1;

        if W[start][i] != float('INF'):
            edgeToVStart += 1;

    length[start] = -1; #start length는 -1로 제외시키기
    save_length[start-1] = 0;

    for _ in range(N-1): #N-1회 반복
        min = float('INF');
        vnear = -1;
        for vertex in range(1,N+1): #1부터 N까지 반복  - 제일 작은 distance를 가지는 vertexFrom / vertexTo 찾기
            if(min > length[vertex] and length[vertex] != -1): #-1인 length를 가지는 vertex는 이미 선택한 vertex임.
                min = length[vertex];
                vnear = vertex;

        selected_edge = [touch[vnear], vnear]; #touch[vnear] -> vnear edge 선택
        edges.append(selected_edge); #edges에 추가
        Y.append(vnear); # Y에 선택된 vertex 추가

        #거리 갱신하기
        for i in range(1,N+1): #1부터 N까지
            if(length[vnear] + W[vnear][i] < length[i]):
                NoC += 1;
                length[i] = length[vnear] + W[vnear][i];
                touch[i] = vnear;

        save_length[vnear - 1] = length[vnear]; # length 저장
        length[vnear] = -1; # 선택된 vnear은 -1로 제외시키기


    print("=" * 10 , " 선택된 Node 순서 ", "=" * 10);
    print(Y);

    print("=" * 10, " save length ", "=" * 10);
    for node in Y:
        print(save_length[node -1], end=' ');
    print();

    print("=" * 10, " 선택된 edge 순서 ", "=" * 10);
    for edge in edges:
        print(edge[0], " - " , edge[1]);

    print("=" * 10, " 가능한 최대 NoC ", "=" * 10);
    print("Max NoC = " , M - edgeToVStart);

    print("=" * 10, " 실제 NoC ", "=" * 10);
    print("real NoC = ", NoC);






# === main function ===#
# ==== 동적으로 입력받는 코드 ====
# N,M,X = map(int(input().split()));
# W = [[float('INF') for _ in range(N+1)] for _ in range(N+1)];
#
# for _ in range(M):
#     fromV,toV,weight = map(int,input().split());
#     W[fromV][toV] = weight;

N = 5; M = 9;#edge 수
W = [[float('INF') for _ in range(N+1)] for _ in range(N+1)];

W[1][2] = 15; W[1][3] = 4; W[1][4] = 11; W[1][5] = 5;
W[2][4] = 1
W[3][2] = 4; W[3][4] = 2;
W[5][2] = 3; W[5][4] = 1;

dijkstra(1);





