#baekjoon_1091_카드 섞기

#=== import module ===#

#=== Function define ===#
def shuffleCardSet(N):
  global S; global num_card; global count;
  count += 1;

  tmpList = [0 for i in range(num_card)];

  for i in range(num_card):
    tmpList[S[i]] = N[i];
  
  for i in range(num_card):
    N[i] = tmpList[i];

def checkCardSet(N):
  global P; global num_card; global originSet;

  if N == originSet: #다시 기존으로 돌아옴.
    return 0;

  tmpList = [0 for i in range(num_card)];
  for i in range(num_card):
    tmpList[N[i]] = i % 3;

  
  if tmpList == P:
    return 1;
  else:
    return -1;


  

#=== variable declare ===#
num_card = 0; P = []; S = []; count = 0;

#=== main function ===#
num_card = int(input());
P = list(map(int,input().split()));
S = list(map(int,input().split()));

originSet = [i for i in range(num_card)];
if [i % 3 for i in range(num_card)] == P:
  print(0);
  exit(0);

N = [i for i in range(num_card)];
success = False;
while(not success):
  shuffleCardSet(N);
  
  checkVal = checkCardSet(N);
  if checkVal == 1:
    success = True;
  elif checkVal == 0:
    break;
  elif checkVal == -1:
    continue;
  
if success:
  print(count);
else: 
  print(-1);
  

  

  