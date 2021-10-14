# baekjoon_1034_램프

def ReturnZeroNum(rampRow):
    cnt = 0;
    for val in rampRow:
        if val == 0: cnt += 1;
    return cnt;

def FindingMax():
    global maxVal #글로벌 변수 사용 선언

    for i in range(row):
        zeroCnt = ReturnZeroNum(ramp_map[i]);
        result = 0;
        #꺼져있는 스위치 개수가 switch 조작 횟수보다 적어야 하는 동시에 스위치 조작 개수랑 짝수/홀수 같아야 함.
        if zeroCnt <= num_switch and zeroCnt % 2 == num_switch % 2:
            for j in range(row):
                if ramp_map[i] == ramp_map[j]:
                    result += 1;
                    maxVal = max(maxVal,result);







row, col = map(int, (input().split()));

ramp_map = [[0 for i in range(col)] for j in range(row)];

for i in range(row):
    ramp_map[i] = list(map(int, list(input())));

num_switch = int(input());

maxVal = 0;

FindingMax();
print(maxVal);
