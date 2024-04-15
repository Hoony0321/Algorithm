def solution(k, dungeons):
    global maxCount
    maxCount = 0
    visited = [False for _ in range(len(dungeons))]
    
    def exploring(k, visited, dungeons, count):
        global maxCount
        maxCount = max(count, maxCount)
        if(len(visited) == dungeons):
            return

        for i in range(len(dungeons)):
            minFatigue, useFatigue = dungeons[i]
            if(visited[i]): continue
            if(k < minFatigue): continue

            visited[i] = True
            exploring(k-useFatigue, visited, dungeons, count+1)
            visited[i] = False
    
    exploring(k, visited, dungeons, 0)
    
    return maxCount