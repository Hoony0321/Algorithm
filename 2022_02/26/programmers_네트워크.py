#programmers_네트워크

#=== import module ===#

#=== variable declare ===#

#=== Function define ===#
def solution(n, computers):
    visited = [False for _ in range(n)];
    global answer;
    answer = 0;
    
    #DFS정의
    def DFS(current, visited, first):
        global answer
        if first: 
          answer += 1; first = False; #새로운 영역 시작

      
        for idx in range(len(computers[current])):
          if computers[current][idx] == 0: continue; #연결 안 됨.
          if visited[idx]: continue; #이미 방문함.
          visited[idx] = True;
          DFS(idx,visited,False);
        
        
    for i in range(n):
        if visited[i]: continue; #이미 방문함.
        visited[i] = True;
        DFS(i,visited,True);
    
    return answer
      

    
    


#=== main function ===#
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]));


