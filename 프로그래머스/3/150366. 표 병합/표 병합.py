def solution(commands):
    answer = []
    map_dict = dict()
    for r in range(1,51):
        for c in range(1,51):
            map_dict[(r,c)] = [(r,c),None] # parent, value
    
    def update1(r,c,value):
        parent = map_dict[(r,c)][0]
        map_dict[parent][1] = value
        
    def update2(value1,value2):
        for key in map_dict.keys():
            parent = map_dict[key][0]
            if map_dict[parent][1] == value1:
                map_dict[parent][1] = value2
    
    def merge(r1,c1,r2,c2):
        p1 = map_dict[(r1,c1)][0]
        p2 = map_dict[(r2,c2)][0]
        
        map_dict[p2][0] = p1
        map_dict[p1][1] = map_dict[p1][1] if map_dict[p1][1] != None else map_dict[p2][1]
        
        for i in range(1,51):
            for j in range(1,51):
                if map_dict[(i,j)][0] == p2:
                    map_dict[(i,j)][0] = p1
                    map_dict[(i,j)][1] = map_dict[p1][1]
        
    
    def unmerge(r,c):
        parent = map_dict[(r,c)][0]
        value = map_dict[parent][1]
        for i in range(1,51):
            for j in range(1,51):
                if map_dict[(i,j)][0] == parent:
                    map_dict[(i,j)][0] = (i,j)
                    map_dict[(i,j)][1] = None
        
        map_dict[(r,c)][1] = value
    
    def _print(r,c):
        parent = map_dict[(r,c)][0]
        value = map_dict[parent][1] if map_dict[parent][1] != None else "EMPTY"
        answer.append(value)
    
    for command in commands:
        command = command.split(" ")
        if command[0] == "UPDATE":
            if len(command) == 4:
                update1(int(command[1]), int(command[2]), command[3])
            else:
                update2(command[1],command[2])
        elif command[0] == "MERGE":
            merge(int(command[1]), int(command[2]), int(command[3]), int(command[4]))
        elif command[0] == "UNMERGE":
            unmerge(int(command[1]), int(command[2]))
        elif command[0] == "PRINT":
            _print(int(command[1]), int(command[2]))
        
            
    return answer