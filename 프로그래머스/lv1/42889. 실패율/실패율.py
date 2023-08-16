def solution(N, stages):
    arrival_list = [[i,0] for i in range(N+2)]
    
    for stage in stages:
        arrival_list[stage][1] += 1
        
    #실패율 계산
    for i in range(1,N+1):
        stage_user = arrival_list[i][1]
        pass_user = sum([x[1] for x in arrival_list[i:]])
        failure_rate = 0 if pass_user == 0 else stage_user/pass_user * 100
        arrival_list[i].append(failure_rate)
    
    #내림차순 정렬
    arrival_list = arrival_list[1:N+1]
    arrival_list.sort(key = lambda x : x[2], reverse=True)
    
    answer = [x[0] for x in arrival_list]
    return answer