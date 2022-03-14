#baekjoon_2023_신기한 소수

# === import module ===#
import math
# === variable declare ===#
dp = {}; dp[2] = True;
# === Function define ===#

def isPrime(num):
    if num not in dp:
        success = False;
        for i in range(2, math.floor(math.sqrt(num))+1): #2부터 sqrt(num)까지 진행
            if num % i == 0: #나누어 떨어짐.
                dp[num] = False; success = True; break;
        if not success: dp[num] = True;
    return dp[num];

def DFS(level, numArr):
    global N;

    if level == N + 1: #종료 조건z
        print("".join(map(str,numArr)));
        return;


    if level == 1: # 맨 앞자리에 숫자 넣기 - 앞 자리는 2,3,5,7,만 가능
        DFS(level+1, numArr + [2]);
        DFS(level + 1, numArr + [3]);
        DFS(level + 1, numArr + [5]);
        DFS(level + 1, numArr + [7]);

    elif level == N: #마지막 자리에 숫자 넣기 소수는 홀수만 가능 - 1,3,5,7,9 가능
        for i in [1,3,5,7,9]:
            tmpNumArr = numArr[:];
            tmpNumArr.append(i);
            result = "";
            for num in tmpNumArr:
                result += str(num);

            if not isPrime(int(result)): continue;
            else: DFS(level+1,numArr + [i]);

    else: #그 외 자리들 넣기 - 넣은 후 판별까지 해야 함.
        for i in range(0,10):
            tmpNumArr = numArr[:];
            tmpNumArr.append(i);
            result = "";
            for num in tmpNumArr:
                result += str(num);

            if not isPrime(int(result)): continue;
            else: DFS(level+1,numArr + [i]);



# === main function ===#
N = int(input());

DFS(1,[]);

