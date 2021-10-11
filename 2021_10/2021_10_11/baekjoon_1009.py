#baekjoon_1009_분산처리

testCsae = int(input());


for test in range(testCsae):
  a,b = map(int,input().split());
  
  last_digit = a%10;
  stage = 1; #stage 선언
  while(stage < b):
    stage += 1; #stage 다음 단계 시작
    last_digit = (last_digit * a)%10;

  if(last_digit == 0): last_digit = 10;
  print(last_digit);

