#programmers_조이스틱

#=== import module ===#

#=== variable declare ===#

#=== Function define ===#
def solution(name):
  alphaList = [chr(i) for i in range(65,91)];
  transList = []; #바꿔야 하는 문자 인덱스 배열

  for idx in range(len(name)):
    if name[idx] != 'A': transList.append(idx);
  print(transList)
  move = 0;
  cur_pos = 0;
  while(1):

    if cur_pos in transList: #현재 위치 문자 바꿔야 함.
      moveChr = ord(name[cur_pos]) - 65;
      if moveChr > 12:
        moveChr = 26 - moveChr;
      move += moveChr;
      transList.remove(cur_pos);
      if len(transList) == 0: break; #종료 조건



    #가장 가까운 거리에 있는 바꿔야 할 문자열 찾기
    #정방향 계산
    if cur_pos > transList[0]:
      dist1 = len(name)-1 - cur_pos + transList[0] +1;
    else:
      dist1 = transList[0] - cur_pos;
    #역방향 계산
    if cur_pos > transList[-1]:
      dist2 = cur_pos - transList[-1];
    else:
      dist2 = cur_pos + len(name)-1 - transList[-1] + 1;

    if dist1 <= dist2:
      move += dist1;
      #print("현위치 {} 정방향 {}".format(cur_pos,dist1));
      cur_pos = transList[0];
    else:
      move += dist2;
      #print("현위치 {} 역방향 {}".format(cur_pos,dist2));
      cur_pos = transList[-1];

  return move;
    

#=== main function ===#
print(solution("ABAAAAAAAAABB"));


