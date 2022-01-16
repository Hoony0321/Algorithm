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

  #구간찾기 시작
  for S in timetable:
    line1 = [S[0], S[0] + 999]; 
    line2 = [S[1], S[1] + 999];

    count = 0;
    for other in timetable:
      if line1[0] <= other[1] and line1[1] >= other[0]:
        count += 1;
    max_count = max(max_count,count);

    count = 0;
    for other in timetable:
      if line2[0] <= other[1] and line2[1] >= other[0]:
        count += 1;
    max_count = max(max_count,count);
  

  return max_count;

print(solution( 	[
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]));