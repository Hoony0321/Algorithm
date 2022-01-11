#kakao_recruitment_2018_1차 셔틀버스
from collections import deque

def convertTime(timeStr):
  _hour = int(timeStr[0:2]) * 60;
  _min = int(timeStr[3:5]);
  return _hour + _min;

def revertTime(timeInt):
  _hour = timeInt // 60;
  _min = timeInt % 60;

  return str(_hour).rjust(2,'0') + ":" + str(_min).rjust(2,'0');

def solution(n, t, m, timetable): #모든 시간은 분으로 환산해서 계산
  answer = ''
  timetable.sort();
  timetable = deque(timetable); #timetable deque로 변환
  shuttle = {}; #shuttle 딕셔너리 형식 -> 도착시간 : 탑승 인원 시간
  for i in range(n):
    arriveTime = 9 * 60 + t * i;
    shuttle[arriveTime] = [];
    for j in range(m):
      if len(timetable) > 0:
        waitingPerson = convertTime(timetable[0]);
        if waitingPerson <= arriveTime: #도착시간보다 먼저 도착했을 경우 -> 탑승
          shuttle[arriveTime].append(waitingPerson);
          timetable.popleft();
        else: #탑승X
          pass;
      else: break;

  lastShuttle = shuttle[arriveTime];
  if len(lastShuttle) < m: #마지막 셔틀에 정원이 남았을 경우
    answer = arriveTime; #도착시간에 오면 됨.
  else: #정원이 남지 않았을 경우
    answer = max(lastShuttle) - 1; #제일 늦은 사람보다 1분 더 빨리 오면 됨.

  answer = revertTime(answer);
  return answer

print(solution(10,60,45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]));