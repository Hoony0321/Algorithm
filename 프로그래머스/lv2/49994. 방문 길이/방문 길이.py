def solution(dirs):
    check = []
    cur_pos = [5, 5]
    
    dir_step = {'U' : [-1,0], 'D' : [1,0], 'R' : [0,1], 'L' : [0,-1]}
    for dir in dirs:
        y,x = cur_pos
        dy,dx = dir_step[dir]        
        ny, nx = y + dy, x + dx
        
        if not((0 <= ny < 11) and (0 <= nx < 11)):
            continue
        
        if([[y,x],[ny,nx]] not in check):
            check.append([[y,x],[ny,nx]])
            check.append([[ny,nx],[y,x]])
        
        cur_pos = [ny,nx]
    
    
    return len(check) / 2