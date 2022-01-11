#kakao_recruitment_2018_1차 추석 트래픽 -> 감을 못 잡음.
def convertNum(S,T):
  hour = int(S[0:2]);
  minute = int(S[3:5]);
  second = int(S[6:8]);
  mile = int(S[9:]);
  T = float(T[0:len(T)-1]);
  endTime = mile + second * 1000 + minute * 1000 * 60 + hour * 1000 * 60 * 60;
  startTime = endTime - int(T * 1000) + 1;

  return [startTime,endTime];

def solution(lines): #모든 시간은 mileSecond로 통일
  timetable = [];
  max_count = -1;
  for elem in lines:
    S = elem[11:23];
    T  = elem[24:];
    timetable.append(convertNum(S,T));
  
  timetable.sort(key=lambda x:x[0]);

  curTimeS = timetable[0][0];
  #구간찾기 시작
  while curTimeS + 1000 <= timetable[-1][1]:
    count = 0;
    for other in timetable:
      if curTimeS <= other[1] and curTimeS + 1000 >= other[0]: #사이에 존재
        count += 1;
    if count > max_count : max_count = count;
    curTimeS += 1000;
  



  
    



  return max_count;

print(solution( 	["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]));