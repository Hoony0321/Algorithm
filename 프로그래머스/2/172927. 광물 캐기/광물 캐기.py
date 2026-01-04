from collections import deque
def solution(picks, minerals):
    answer = 0
    
    # init dict
    mineral_dict = dict()
    mineral_dict['diamond'] = 0
    mineral_dict['iron'] = 1
    mineral_dict['stone'] = 2
    
    fatigue_dict = dict()
    fatigue_dict['diamond'] = [1,1,1]
    fatigue_dict['iron'] = [5,1,1]
    fatigue_dict['stone'] = [25,5,1]
    
    # init dp
    dp = [[[float('inf') for _ in range(6)] for _ in range(6)] for _ in range(6)]
    dp[picks[0]][picks[1]][picks[2]] = 0
    
    # init queue
    queue = deque()
    state = [0] + picks
    queue.append(state)
    
    # main process
    while queue:
        mineral_idx,diamond,iron,stone = queue.popleft()
        fatigue = dp[diamond][iron][stone]
        
        if mineral_idx >= len(minerals):
            dp[0][0][0] = min(dp[0][0][0], fatigue)
            continue
        
        count = 0
        mineral = []
        while mineral_idx < len(minerals) and count < 5:
            mineral.append(mineral_dict[minerals[mineral_idx]])
            mineral_idx += 1
            count += 1
            
        
        
        # use diamond
        if diamond > 0:
            _fatigue = fatigue
            for elem in mineral:
                _fatigue += fatigue_dict['diamond'][elem]

            if _fatigue < dp[diamond-1][iron][stone]:
                dp[diamond-1][iron][stone] = _fatigue
                queue.append([mineral_idx,diamond-1,iron,stone])
        
        # use iron
        if iron > 0:
            _fatigue = fatigue
            for elem in mineral:
                _fatigue += fatigue_dict['iron'][elem]

            if _fatigue < dp[diamond][iron-1][stone]:
                dp[diamond][iron-1][stone] = _fatigue
                queue.append([mineral_idx,diamond,iron-1,stone])
                
        # use stone
        if stone > 0:
            _fatigue = fatigue
            for elem in mineral:
                _fatigue += fatigue_dict['stone'][elem]

            if _fatigue < dp[diamond][iron][stone-1]:
                dp[diamond][iron][stone-1] = _fatigue
                queue.append([mineral_idx,diamond,iron,stone-1])
        
    return dp[0][0][0]