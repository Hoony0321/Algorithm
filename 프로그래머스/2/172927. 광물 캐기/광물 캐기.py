from collections import deque
from copy import deepcopy

minTotalFatigue = float('INF')
mineralToNumber = {'diamond' : 0, 'iron' : 1, 'stone' : 2}
fatigueGraph = [[1,1,1], [5,1,1], [25,5,1]]

def digMinerals(pick, minerals):
    global minTotalFatigue
    totalFatigue = 0
    
    digCount = 0
    while minerals and digCount < 5:
        mineral = minerals.popleft()
        totalFatigue += fatigueGraph[pick][mineralToNumber[mineral]]
        digCount += 1
    
    return totalFatigue

def dfs(picks, minerals, totalFatigue):
    global minTotalFatigue
    if(totalFatigue >= minTotalFatigue): return
    
    if( #종료조건
        (len(minerals) == 0) or
        (picks[0] == 0 and picks[1] == 0 and picks[2] == 0)
      ): 
        minTotalFatigue = min(minTotalFatigue, totalFatigue)
        return
    
    for i in range(0,3):
        if(picks[i] != 0):
            newPicks = deepcopy(picks)
            newMinerals = deepcopy(minerals)
            newPicks[i] -= 1
            dfs(newPicks, newMinerals, totalFatigue + digMinerals(i, newMinerals))
        

def solution(picks, minerals):
    global minTotalFatigue
    minTotalFatigue = float('INF')
    minerals = deque(minerals)
    dfs(picks, minerals, 0)
    
    return minTotalFatigue