import heapq

def solution(n, edges):
    graph = [[] for _ in range(n)]
    distance = [float('inf')] * n
    visited = [False] * n  # 방문 여부 체크를 위한 배열

    # 그래프를 인접 리스트로 구성
    for u, v in edges:
        graph[u-1].append((v-1, 1))  # 가중치가 1인 간선 추가
        graph[v-1].append((u-1, 1))  # 양방향 그래프를 가정

    def dijkstra(start):
        queue = [(0, start)]  # (거리, 노드)
        distance[start] = 0

        while queue:
            dist, current_node = heapq.heappop(queue)
            if visited[current_node]:  # 이미 방문한 노드는 스킵
                continue
            visited[current_node] = True

            for next_node, weight in graph[current_node]:
                cost = dist + weight
                if cost < distance[next_node] and not visited[next_node]:
                    distance[next_node] = cost
                    heapq.heappush(queue, (cost, next_node))

    dijkstra(0)  # 0번 노드부터 시작

    # 최대 거리 노드의 수를 계산
    max_distance = max(distance)
    return distance.count(max_distance)