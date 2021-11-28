#baekjoon_9019_DSLR_시간초과

#=== import module ===#
import copy
#=== variable declare ===#
def ReturnFourDigit(num):
  num = str(num);
  if len(num) == 1:
    num = [int(num)];
  else:
    num = list(map(int,num));

  diff = 4 - len(num);
  for _ in range(diff):
    num.insert(0,0);
  

  return num;

def ReturnNum(arr):
  num = arr[0] * (10 ** 3) + arr[1] * (10 ** 2) + arr[2] * 10 + arr[3];
  return num;

#=== Function define ===#
def BFS(A,B):
  queue = [[A,[]]];
  result = [];
  while(queue):
    
    peek = queue.pop(0);
    
    curNum = peek[0];
    curProcess = peek[1];

    if curNum == B:
      result = curProcess;
      break;
    #D 2배 -> 9999보다 크면 10000으로 나눈 나머지
    if curNum != [0,0,0,0]:
      tmpNum = ReturnNum(curNum);
      tmpNum = tmpNum * 2;
      if tmpNum > 9999:
        tmpNum = tmpNum % 10000;
      nextNum = ReturnFourDigit(str(tmpNum));
      curProcess.append('D');
      queue.append([nextNum,copy.deepcopy(curProcess)]);
      del curProcess[-1];

    #S -1 -> 0이면 9999
    tmpNum = ReturnNum(curNum);
    if tmpNum == 0:
      tmpNum = 9999;
    else:
      tmpNum = tmpNum - 1;
    nextNum = ReturnFourDigit(str(tmpNum));
    curProcess.append('S');
    queue.append([nextNum,copy.deepcopy(curProcess)]);
    del curProcess[-1];


    #L -> 왼쪽으로 자릿수 옮김
    if len(curProcess) == 0 or curProcess[-1] != 'R':
      tmpList = copy.deepcopy(curNum);
      tmpNum = tmpList[0];
      tmpList[0] = tmpList[1]; tmpList[1] = tmpList[2]; 
      tmpList[2] = tmpList[3]; tmpList[3] = tmpNum;
      nextNum = tmpList;
      curProcess.append('L');
      queue.append([nextNum,copy.deepcopy(curProcess)]);
      del curProcess[-1];

    #R -> 오른쪽으로 자릿수 옮김
    if len(curProcess) == 0 or curProcess[-1] != 'L':
      tmpList = copy.deepcopy(curNum);
      tmpNum = tmpList[3];
      tmpList[3] = tmpList[2]; tmpList[2] = tmpList[1]; 
      tmpList[1] = tmpList[0]; tmpList[0] = tmpNum;
      nextNum = tmpList;
      curProcess.append('R');
      queue.append([nextNum,copy.deepcopy(curProcess)]);
      del curProcess[-1];

  return result;



#=== main function ===#
T = int(input());

for _ in range(T):
  A,B = input().split();
  A = ReturnFourDigit(A); 
  B = ReturnFourDigit(B);

  result = BFS(A,B);
  for elem in result:
    print(elem, end='');
  print();
    