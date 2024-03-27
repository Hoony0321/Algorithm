from collections import deque

def grouping(cards, groups):
    visited = [False for _ in range(len(cards))]
    
    for i in range(len(cards)):
        if(visited[i]): continue
        visited[i] = True
        group = []
        
        cardIndex = i
        group.append(cardIndex)
        
        while True:
            cardIndex = cards[cardIndex]-1
            if(visited[cardIndex]): break
            visited[cardIndex] = True
            group.append(cardIndex)
        
        groups.append(group)
        
def getBestScore(groups):
    scores = []
    
    for group in groups:
        scores.append(len(group))
    
    scores.sort(reverse=True)
    
    return scores[0] * scores[1]
        
def solution(cards):
    groups = []
    grouping(cards, groups)
    
    if(len(groups) < 2):
        return 0
    
    return getBestScore(groups)