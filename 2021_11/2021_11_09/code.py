#baekjoon_1038_감소하는 수

#=== import module ===#

#=== Function define ===#
def IsdescNum(num):

  global look_for_count;
  global count;
  global isCompleted
  result = True;

  for i in range(len(num)-1):
    if num[i] <= num[i+1]:
      result = False;
      break;
  
  if result:
    count += 1;
    if look_for_count == count:
      isCompleted = True;
  return result;

def recurNum(num, curDigit):
  for i in range(curDigit,len(num)):
    num[i] = 0;
  return;
  

#=== variable declare ===#
look_for_count = 0;
count = 9;
isCompleted = False;
num = [];
k = 2; #현재 자릿수
startDigit = 0; #살펴보고 있는 자릿수
curDigit = 0;
#=== main function ===#
look_for_count = int(input());

if look_for_count <= 9:
  print(look_for_count);
  exit(0);

while(not isCompleted):

  num = [0 for _ in range(k)];
  startDigit = 0;
  while(not isCompleted):
    if num[0] == 9: #해당 자릿수 탐색 완료
      break;

    curDigit = startDigit
    while(not isCompleted):
      num[curDigit] += 1;

      if IsdescNum(num): #감소하는 수 맞음
        if curDigit != len(num) -1: #마지막 수가 아니면 자릿수 증가
          curDigit += 1;
          continue;
      else: #감소하는 수 아님
        if curDigit+2 < len(num) and num[curDigit+1] == 0 and num[curDigit+2] == 0:
          startDigit = curDigit+1;
        else:
          recurNum(num,curDigit);
          startDigit = curDigit -1;
        break; #while문 탈출 다시 startDigit부터 시작
      

  k += 1; #다음 자릿수로 넘어가서 탐색

print(num);

  
  
  




