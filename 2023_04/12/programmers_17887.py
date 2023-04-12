#문제설명
#프로그래머스 달리기

def solution(players, callings):
    
    playerMap = {}
    for idx,player in enumerate(players):
        playerMap[player] = idx
    
    for name in callings:
        idx = playerMap[name]
        idx2 = playerMap[players[idx-1]]
        
        playerMap[name], playerMap[players[idx-1]] = idx2, idx
        players[idx-1], players[idx] = players[idx], players[idx-1]
    
    
    return players