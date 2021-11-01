#baekjoon_1013_Contact
def checkVegaSignal(signal,idx):
  #(100+1+ | 01)+ 형식의 신호인지 판단하는 함수
  if(idx == len(signal)):
    return True;
  chkIdx = idx;
  if(signal[idx] == '1'): #(100+1+)인 경우
    if(idx+3 >= len(signal)): return False;
    if(signal[idx:idx+3] == '100'): #앞부분이 100이 일 경우만 가능
      chkIdx = signal.find('1',idx+3); #1인 부분
      if chkIdx != -1: # 못 찾을 경우 제외
        num1idx = 0;
        for i in range(chkIdx+1,len(signal)):
          if(signal[i] != '1'): break;
          else: num1idx = i;
        #100_1+인 경우
          checkVegaSignal(signal,num1idx+1);
        #100_1+100인 경우
          checkVegaSignal(signal,num1idx);
      else:
        return False;
    else:
      return False;
  else: #(01)인 경우
    if(idx+1 >= len(signal)): return False;
    if(signal[idx+1] == '1'):
      checkVegaSignal(signal,idx+2);
    else:
      return False;

testCase = int(input());

for case in range(testCase):
  signal = input();
  if checkVegaSignal(signal,0):
    print("YES");
  else:
    print("NO");