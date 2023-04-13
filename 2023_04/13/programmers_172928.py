#문제정보
#programmers_172928 - 공원 산책

def solution(park, routes):
    answer = []
    curPos = [0,0]
    moveDest = { "N" : [-1,0], "S" : [+1, 0], "W" : [0,-1], "E" : [0,+1]}
    
    def move(dest, n, curPos):
        ny, nx = curPos
        isMove = True
        for _ in range(int(n)):
            ny += moveDest[dest][0]
            nx += moveDest[dest][1]
            
            if(nx < 0 or nx >= len(park[0]) or ny < 0 or ny >= len(park)):
                isMove = False
                break;
            if(park[ny][nx] == "X"): 
                isMove = False
                break;
            
        if(isMove): 
            curPos[0] = ny
            curPos[1] = nx
    
    find = False
    for i in range(len(park)):
        if(find): break;
        for j in range(len(park[i])):
            if(park[i][j] == "S"):
                curPos = [i,j]
                find = True
                break;
    
    for index, route in enumerate(routes):
        dest, n = route.split()
        move(dest, n, curPos)
    
    answer = curPos
    
    return answer