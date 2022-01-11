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

  curTimeS = -1;
  for targetTime in timetable:
    target_startTime = targetTime[0]; target_endTime = targetTime[1];

    if curTimeS > target_startTime: continue;

    curTimeS = target_startTime;
    #구간찾기 시작
    while curTimeS <= target_endTime:
      count = 0;
      for other in timetable:
        if curTimeS <= other[0] and other[1] <= curTimeS +1000: #사이에 존재
          count += 1;
      if count > max_count : max_count = count;
      curTimeS += 1;
    curTimeS -= 1; #마지막에 증가한 시간은 적용 X -> 아직 탐색 안 함.
  
  print(max_count);


  
    



  return 0;

solution( [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]);