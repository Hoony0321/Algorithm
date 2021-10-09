#baekjoon_1015_수열정렬

class Point:
  def __init__(self,_val, _idx):
    self.value = _val;
    self.index = _idx;
    self.rank = -1;
  
  def setRank(self,_rank):
    self.rank = _rank;
  
  def __gt__(self,other):
    return self.value > other.value;

  def __str__(self):
    return str(self.value);

  

N = int(input());
tempList = list(map(int,input().split()));
A = [];
for i in range(N):
  A.append(Point(tempList[i],i));

#정렬
for i in range(N-1):
  min = i
  for j in range(i+1,N):
    if A[min] > A[j]: min = j;
  #최솟값 index 값이랑 i번째 값이랑 스왑
  A.insert(i,A[min]);
  del A[min+1];

for i in range(N):
  A[i].setRank(i);

#다시 정렬
for i in range(N-1):
  min = i;
  for j in range(i+1,N):
    if A[min].index > A[j].index: min = j;
  #최솟값 index 값이랑 i번째 값이랑 스왑
  A.insert(i,A[min]);
  del A[min+1];

for item in A:
  print(item.rank, end=' ');