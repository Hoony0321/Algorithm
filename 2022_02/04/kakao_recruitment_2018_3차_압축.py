#kakao_recruitment_2018_3차_압축

def solution(msg):
  indexArr = [];
  lib = [chr(i) for i in range(64,91)];

  while(1):

    max_count = 0;
    selected_idx = -1;

    #제일 많은 중복을 가진 문자열 찾기
    for idx in range(1,len(lib)):
      target = lib[idx];
      count = 0;
      while(1):
        
        if not (count < len(msg) and count < len(target)): break;
        if msg[count] == target[count]: 
          count += 1;
        else: break;
      
      if count > max_count:
        selected_idx = idx;
        max_count = count;

    indexArr.append(selected_idx); #해당 인덱스 추가

    if len(msg) == len(lib[selected_idx]): #완벽하게 동일한 문자열인 경우
      break;
    else: #동일한 문자열 아님 -> 끝에 다음 문자 추가해서 색인 등록
      add_msg = msg[0:max_count+1] #0부터 count+1까지해서 추가
      lib.append(add_msg);
      #문자열 바꾸기
      msg = msg[max_count:];
  
  return indexArr;

print(solution('ABABABABABABABAB'));


    
    
      


