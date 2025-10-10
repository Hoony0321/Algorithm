def solution(commands):
    answer = []
    parents = [[[r,c] for c in range(51)] for r in range(51)]
    board = [[None for _ in range(51)] for _ in range(51)]
    
    def find(r,c):
        if parents[r][c] != [r,c]:
            parents[r][c] = find(parents[r][c][0], parents[r][c][1])
        return parents[r][c]
    
    def union(r1,c1,r2,c2):
        p1 = find(r1,c1)
        p2 = find(r2,c2)
        parents[p2[0]][p2[1]] = p1
    
    def update1(r,c,value):
        p = find(r,c)
        board[p[0]][p[1]] = value
    
    def update2(value1, value2):
        for r in range(1,51):
            for c in range(1,51):
                pr,pc = find(r,c)
                if board[pr][pc] == value1:
                    board[pr][pc] = value2
    
    def merge(r1,c1,r2,c2):
        if r1 == r2 and c1 == c2:
            return
        
        # 병합
        p1 = find(r1,c1)
        p2 = find(r2,c2)
        union(p1[0], p1[1], p2[0], p2[1])
        
        # 값 수정
        value1 = board[p1[0]][p1[1]]
        value2 = board[p2[0]][p2[1]]
        board[p1[0]][p1[1]] = value1 if value1 else value2
    
    def unmerge(r,c):
        p = find(r,c)
        v = board[p[0]][p[1]]
        unmerge_arr = []
        
        for _r in range(1,51):
            for _c in range(1,51):
                _p = find(_r,_c)
                if p == _p:
                    # 병합 해제
                    unmerge_arr.append([_r,_c])
                    board[_r][_c] = None
        
        for y,x in unmerge_arr:
            parents[y][x] = [y,x]
        
        board[r][c] = v
    
    def _print(r,c):
        pr,pc = find(r,c)
        value = board[pr][pc] if board[pr][pc] else "EMPTY"
        answer.append(value)
    
    for command in commands:
        c = command.split()
        n = len(c)
        
        if c[0] == "UPDATE":
            if n == 4:
                update1(int(c[1]), int(c[2]), c[3])
            if n == 3:
                update2(c[1], c[2])
        elif c[0] == "MERGE":
            merge(int(c[1]), int(c[2]), int(c[3]), int(c[4]))
        elif c[0] == "UNMERGE":
            unmerge(int(c[1]), int(c[2]))
        elif c[0] == "PRINT":
            _print(int(c[1]), int(c[2]))
    
    return answer