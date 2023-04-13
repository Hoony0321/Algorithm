#문제 정보
#programmers - 바탕화면 정리 - 난이도 1

def solution(wallpaper):
    answer = []
    
    lux, luy, rdx, rdy = 51, 51,-1,-1
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if(wallpaper[i][j] == "#"):
                if(j < lux) : lux = j
                if(j+1 > rdx) : rdx = j+1
                if(i < luy) : luy = i
                if(i+1 > rdy) : rdy = i+1
    
    answer = [luy, lux, rdy, rdx]
                
                
    return answer