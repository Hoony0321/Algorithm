#baekjoon_1059_좋은 구간

#=== import module ===#

#=== Function define ===#
#범위 => start, end 포함
def FindSection(start,end,num):
  count = 0;
  for i in range(start,end):
    for j in range(i+1,end+1):
      if i <= num <= j:
        count += 1;
  
  return count;

#=== variable declare ===#
length = 0;
S = [];
N = 0;
index = -1; #N이 S배열에 들어갈 위치

#=== main function ===#
length = int(input());
S = list(map(int,input().split()));
N = int(input());

#S배열 정렬
S.sort()

#index 위치 찾기
for i in range(length):
  if N < S[i]:
    index = i;
    break;
  elif N == S[i]:
    index = -1;
    break;
  elif N > S[i]:
    index = i+1;
result = -1;
if index == -1:
  result = 0;
elif index == 0:
  result = FindSection(1,S[index]-1,N);
else:
  result = FindSection(S[index-1]+1, S[index]-1, N);

print(result);
  
  

  