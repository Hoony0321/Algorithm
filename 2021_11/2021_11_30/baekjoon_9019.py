#baekjoon_9019_DSLR_시간초과
#deque가 핵심 해결법 -> append/pop가 O(N)이 아닌 O(1)
#=== import module ===#
import copy
from collections import deque
#=== variable declare ===#


#=== Function define ===#
def BFS(A,B):

  queue = deque();
  queue.append([A,""]);
  result = "";
  dp = [False for i in range(10000)];
  
  while(queue):
    peek = queue.popleft();
    curNum = peek[0];
    curProcess = peek[1];

    if curNum == B:
      result = curProcess;
      break;

    d1 = curNum // 1000;
    d2 = (curNum % 1000) // 100;
    d3 = (curNum % 100) // 10;
    d4 = curNum % 10;

    
    #D 2배 -> 9999보다 크면 10000으로 나눈 나머지
    if curNum != 0:
      tmpNum = curNum * 2;
      if tmpNum > 9999:
        tmpNum = tmpNum % 10000;    
      if not dp[tmpNum]:
        dp[tmpNum] = True;
        queue.append([tmpNum,curProcess + "D"]);


      

    #S -1 -> 0이면 9999
    if curNum == 0:
      tmpNum = 9999;
    else:
      tmpNum = curNum - 1;
    if not dp[tmpNum]:
      dp[tmpNum] = True;
      queue.append([tmpNum,curProcess + "S"]);


    #L -> 왼쪽으로 자릿수 옮김
    tmpList = [d2,d3,d4,d1]; #1234 -> 2341
    tmpNum = d2 * 1000 + d3 * 100 + d4 *10 + d1;
    if not dp[tmpNum]:
      dp[tmpNum] = True;
      queue.append([tmpNum,curProcess + "L"]);

    #R -> 오른쪽으로 자릿수 옮김
    tmpList = [d4,d1,d2,d3]; #1234 -> 4123
    tmpNum = d4 * 1000 + d1 * 100 + d2 *10 + d3;
    if not dp[tmpNum]:
      dp[tmpNum] = True;
      queue.append([tmpNum,curProcess + "R"]);

  return result;



#=== main function ===#
T = int(input());

for _ in range(T):
  A,B = map(int,input().split());

  print(BFS(A,B));

    