#baekjoon_1039_교환

# === import module ===#

# === variable declare ===#
N = None; #숫자
K = None; #연산 횟수
# === Function define ===#
def Swap(inputIdx, targetIdx):
    tmp = number[inputIdx];
    tmpN = number[:];

    tmpN[inputIdx] = tmpN[targetIdx];
    tmpN[targetIdx] = tmp;

    result = 0;

    for i in range(len(tmpN)):
        result += int(tmpN[i]) * (10 ** (len(tmpN) - 1 - i));

    return result;

# === main function ===#
N,K = input().split(); K = int(K);
number = [];
M = len(N);
for i in range(M):
    number.append(int(N[i]));

current = 0; #정렬이 안 된 부분
for _ in range(K):

    #제일 큰 수 찾기
    max_num = -1;
    max_arr = [];
    for i in range(M):
        if number[i] > max_num:
            max_num = number[i];
            max_arr.clear();
            max_arr.append(i);
        elif number[i] == max_num:
            max_arr.append(i);

    #들어갈 자리 찾기
    inputIdx = -1;
    for i in range(current,M):
        if number[i] < max_num:
            inputIdx = i;
            break;

    #숫자 대입 해보기
    testArr = [];
    for _ in range(len(max_arr)):
        for idx in max_arr:
            testArr.append(Swap(inputIdx,idx));

    testArr.sort();

    tmpNumber = str(testArr[-1]);

    number.clear();
    for i in range(M):
        number.append(int(tmpNumber[i]));

print(number);
