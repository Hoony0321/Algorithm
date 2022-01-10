#kakao_recruitment_2018_1차 뉴스 클러스터링
import math
def solution(str1, str2):
    answer = 0
    str1 = str1.lower(); str2=str2.lower(); #대소문자 무시.
    str1 = list(str1); str2 = list(str2); #다루기 편하게 리스트화
    setA = []; setB = []; #str1,str2 집합 배열
    intersection = []; #AnB 집합 배열

    #두글자씩 끊어서 집합 만들기
    beforeChar = None;
    for i in range(0,len(str1)):
      if str1[i].isalpha(): #알파벳인 경우
        if beforeChar != None:
          setA.append(beforeChar + str1[i]);
        beforeChar = str1[i];
      else: #알파벳이 아닌 경우
        beforeChar = None;
      
    beforeChar = None;
    for i in range(0,len(str2)):
      if str2[i].isalpha(): #알파벳인 경우
        if beforeChar != None:
          setB.append(beforeChar + str2[i]);
        beforeChar = str2[i];
      else: #알파벳이 아닌 경우
        beforeChar = None;
    
    if len(setA) == 0 and len(setB) == 0: return 65536;
    
    #ANB 구하기
    interIdx = [False for _ in range(len(setB))];
    for i in range(0,len(setA)):
      for j in range(0,len(setB)):
        if interIdx[j]: continue;

        if setA[i] == setB[j]:
          interIdx[j] = True;
          intersection.append(setA[i]);
          break;
    
    
    #계산하기
    temp = len(intersection) / (len(setA) + len(setB) - len(intersection))
    answer = math.floor(temp * 65536);

    
    
    return answer

print(solution("E=M*C^2","e=m*c^2"));