#programmers_여행경로

#=== import module ===#
from collections import deque
from copy import deepcopy
#=== variable declare ===#

#=== Function define ===#

  

def solution(tickets):
  queue = deque();
  queue.append(["ICN",[]]) #현재 위치, 사용한 티겟 정보
  answer = [];
  while queue:
    current,used = queue.popleft();
    if len(used) == len(tickets): #모든  티겟 사용 - 종료조건
      answer.append(used);
    else:
      for idx in range(len(tickets)):
        if idx in used: continue; #이미 사용한 티겟

        ticket_info = tickets[idx];
        if ticket_info[0] != current: continue; #현위치에서 출발하는 티겟 아님.
        
        tmpUsed = deepcopy(used); #깊은 복사
        tmpUsed.append(idx);
        queue.append([ticket_info[1],tmpUsed]);

  #경로 번호를 이름으로 바꿔주는 함수
  def ConvertToName(route):
    tmpArr = ["ICN"];
    for elem in route:
      tmpArr.append(tickets[elem][1]);
    return tmpArr;
  
  for idx in range(len(answer)):
    answer[idx] = ConvertToName(answer[idx]);

  return(min(answer));

    
    
#=== main function ===#
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]);


