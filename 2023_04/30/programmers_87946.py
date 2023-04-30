#문제설명
#programmers_87946 - 피로도 (난이도 2)

from collections import deque
def solution(k, dungeons):
    answer = 0
    stack = deque([])
    
    init_stat = [k, 0, [False for _ in range(len(dungeons))]]
    stack.append(init_stat)
    
    while stack:
        k, n, visited = stack.popleft()
        if(n > answer): answer = n
        
        for i in range(len(visited)):
            if(not visited[i]): #방문 안 한 곳이 있다면
                if(k >= dungeons[i][0]):
                    _visited = visited.copy()
                    _visited[i] = True
                    stack.append([k - dungeons[i][1], n+1, _visited])
        
    

    return answer