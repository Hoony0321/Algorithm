#kakao_recruitment_2018_3차_방금그곡
def convertTimeToNum(start,end):
  H_start, M_start = map(int,start.split(":"));
  H_end, M_end = map(int,end.split(":"));

  return (H_end * 60 + M_end) - (H_start * 60 + M_start);

def convertScores(minutes,scores):
  scores = list(scores);
  length = len(scores);
  re_scores = "";
  for i in range(minutes):
    re_scores += scores[i%length];
  
  return re_scores;

def convertSemi(scores):
  scores = list(scores);
  re_scores = "";
  continue_if = False;
  for i in range(len(scores)):
    if continue_if: continue_if = False; continue;
    if i+1 < len(scores) and scores[i+1] == "#":
      re_scores += scores[i].lower();
      continue_if = True;
    else:
      re_scores += scores[i];
  
  return re_scores;

def solution(m, musicinfos):
  
  #musicinfos data refine.
  for i in range(len(musicinfos)):
    start,end,title,scores = musicinfos[i].split(",");
    minutes = convertTimeToNum(start,end);
    scores = convertSemi(scores);
    scores = convertScores(minutes,scores);
    musicinfos[i] = [minutes,title,scores];

  #길이 기준으로 내림차순 정렬  
  musicinfos.sort(key=lambda x : -x[0]);

  #음 찾기
  m = convertSemi(m);
  target = -1;
  for idx in range(len(musicinfos)):
    if musicinfos[idx][2].find(m) != -1: #찾음
      target = idx; break;
  
  if target == -1: #해당하는 곡 존재하지 않음.
    return "(None)";
  else: #해당하는 곡 존재
    return musicinfos[target][1];
    





print(solution("CC#BCC#BCC#",	["03:00,03:08,FOO,CC#B"]));

    
    