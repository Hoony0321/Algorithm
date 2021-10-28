#baekjoon_1150_백업

def ReturnMaxDistanceIndex(connectLines):
  maxConLine = [-1,-1]; #거리, 인덱스
  for i in range(len(connectLines)):
    if connectLines[i].distance > maxConLine[0]:
      maxConLine[1] = i;
      maxConLine[0] = connectLines[i].distance;
  
  return maxConLine[1];


class connectLine:
  conLine_MAX_index = -1; #가장 distance 큰 line의 index

  def __init__(self,pos1, pos2, distance):
    self.pos1 = pos1;
    self.pos2 = pos2;
    self.distance = distance;
  
  def __str__(self):
    print(self.pos1, self.pos2);
  

def solve(distances, cables):
  num_company = len(distances);
  used_company = [];
  connectLines = [];
  
  for i in range(num_company-1):
    if i in used_company: continue;
    
    for j in range(i+1,num_company):
      if j in used_company: continue;
      conLine = connectLine(i,j,abs(distances[i] - distances[j]));
      if connectLines: #빈 배열 X
        conLine_MAX = connectLines[connectLine.conLine_MAX_index];
        if conLine_MAX.distance > conLine.distance: #더 짧은 거리 발견
          used_company.remove(conLine_MAX.pos1); #used 배열에서 삭제
          used_company.remove(conLine_MAX.pos2); #used 배열에서 삭제
          del connectLines[connectLine.conLine_MAX_index]; # 기존 가장 장거리 원소 삭제
          connectLines.append(conLine);
          connectLine.conLine_MAX_index = ReturnMaxDistanceIndex(connectLines); #가장 거리 긴 원소 인덱스 삽입
          used_company.extend([conLine.pos1,conLIne.pos2]); #used 배열에 추가
      else: #빈 배열
        used_company.extend([conLine.pos1,conLIne.pos2]);
        connectLines.append(conLine);
        connectLine.conLine_MAX_index = 0;







companies,cables = map(int, input().split());

distances = [];
for i in range(companies):
  distance = int(input());
  distances.append(distance);

solve(distances,cables);