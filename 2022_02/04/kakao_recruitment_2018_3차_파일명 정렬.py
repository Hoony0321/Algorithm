#kakao_recruitment_2018_3차_파일명 정렬
from copy import deepcopy
def solution(files):
    originFiles = deepcopy(files);
    #files elements들 [head,number,idx]로 바꾸기
    for idx in range(len(files)):
      elem = []; 
      target = files[idx];
      iter = 0;
      #HEAD part
      while(iter < len(target)):
        if target[iter].isdecimal(): #숫자일 경우 -> head part 끝
          iter -= 1;
          break;
        else: iter += 1;
      head_end = iter;
      elem.append(target[0:head_end+1].lower());
      #NUMBER part
      iter += 1;
      while(iter < len(target)):
        if not target[iter].isdecimal(): #문자일 경우 -> number part 끝
          break;
        else: iter += 1;

      number_end = iter -1;

      elem.append(target[head_end+1:number_end+1]);

      #idx 넣기
      elem.append(idx);

      files[idx] = elem;
    
    #Head 기준으로 정렬
    files.sort(key = lambda x : (x[0], int(x[1])));

    #answer 생성
    answer = [originFiles[files[i][2]] for i in range(len(files))];


    return answer;


    

print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]));