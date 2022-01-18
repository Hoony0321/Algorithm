#kakao_recruitment_2018_1차_뉴스 클러스터링 (파이써닉하게 풀기)
import math
def solution(str1, str2):
  A = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()];
  B = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()];
  
  AllList = set(A) | set(B);

  if AllList:
    set1 = []; #교집합
    set2 = []; #합집합
    for elem in AllList:
      set1.extend([elem] * min(A.count(elem) , B.count(elem)));
      set2.extend([elem] * max(A.count(elem) , B.count(elem)));
    
    result = math.floor(len(set1) / len(set2) * 65536)
  else: result = 65536;

  return result;



print(solution("aa1+aa2","AAAA12"));