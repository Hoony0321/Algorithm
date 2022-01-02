#baekjoon_2579_계단 오르기

#=== import module ===#

#=== variable declare ===#
N = None; #계단 개수
stairs = [0]; #계단 정보
dp = []; #dp 배열
#=== Function define ===#
def UpStair(curStep, prevStep):
  global N;

  if curStep == N: 
    return stairs[curStep]; #종료 조건

  if dp[curStep][prevStep] != None: return dp[curStep][prevStep];

  max_result = 0;
  #계단 1개 오르는 경우
  nextStep = curStep + 1;
  if not(prevStep > 0 and prevStep + 1 == curStep and prevStep + 2 == nextStep): 
    #연속된 계단 3개 ,아닐때 올라감.
    max_result = max(max_result, stairs[curStep] + UpStair(nextStep, curStep)); 

  #계단 2개 오르는 경우
  nextStep = curStep + 2;
  if nextStep <= N:
    max_result = max(max_result, stairs[curStep] + UpStair(nextStep, curStep));

  dp [curStep][prevStep] = max_result;
  return max_result;
  
  

#=== main function ===#
N = int(input());
dp = [[None for _ in range(N+1)] for _ in range(N+1)]
for _ in range(N):
  stairs.append(int(input()));

print(UpStair(0,-1));

