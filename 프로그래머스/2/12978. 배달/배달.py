import heapq
def solution(N, road, K):
    answer = 0
    
    graph = [[] for _ in range(N+1)]
    for edge in road:
        u,v,w = edge
        graph[u].append([v,w])
        graph[v].append([u,w])
    
    queue = []
    distance = [float('inf') for _ in range(N+1)]
    distance[1] = 0
    visited= [False for _ in range(N+1)]
    heapq.heappush(queue, [0,1])
    
    while queue:
        curWeight, curNode = heapq.heappop(queue)
        if(visited[curNode]): continue
        visited[curNode] = True
        
        for info in graph[curNode]:
            nearNode, weight = info
            if(visited[nearNode]): continue
            if(curWeight + weight >= distance[nearNode]): continue
            
            distance[nearNode] = curWeight + weight
            heapq.heappush(queue, [curWeight + weight, nearNode])
    
    for dist in distance:
        if(dist <= K): answer += 1

    return answer