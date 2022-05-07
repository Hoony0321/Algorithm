# 문제 정보 baekjoon_9663_NQueens
#N-Queens problem Algorithm

# === import module ===#

# === variable declare ===#

# === Function define ===#


def queens(index):
    global n, result;

    if(index == n): #마지막 단계이면 result 출력
        result += 1;
    else: #마지막 단계아님.
        for value in range(0,n):
            col[index] = value;
            if checkPromise(index):
                addUsed(index,col[index]);
                queens(index+1); #다음 단계로 진행
                #used 배열 원복하기
                cleanUsed(index, col[index]);

def addUsed(index, value):
    col_used[value] = True;

    tmpIndex = index; tmpValue =value;
    #오른쪽 위끝에 있는 행/열 찾기
    while(tmpIndex > 0 and tmpValue < n-1):
        tmpIndex -= 1;
        tmpValue += 1;
    right_diagonal_used[tmpIndex][tmpValue] = True;


    tmpIndex = index; tmpValue =value;
    # 왼쪽 위끝에 있는 행/열 찾기
    while (tmpIndex > 0 and tmpValue > 0):
        tmpIndex -= 1;
        tmpValue -= 1;
    left_diagonal_used[tmpIndex][tmpValue] = True;

def cleanUsed(index, value):
    col_used[value] = False;

    tmpIndex = index; tmpValue =value;
    #오른쪽 위끝에 있는 행/열 찾기
    while(tmpIndex > 0 and tmpValue < n-1):
        tmpIndex -= 1;
        tmpValue += 1;
    right_diagonal_used[tmpIndex][tmpValue] = False;


    tmpIndex = index; tmpValue =value;
    # 왼쪽 위끝에 있는 행/열 찾기
    while (tmpIndex > 0 and tmpValue > 0):
        tmpIndex -= 1;
        tmpValue -= 1;
    left_diagonal_used[tmpIndex][tmpValue] = False;

def checkRightDiagonal(index, value):
    #오른쪽 위끝에 있는 행/열 찾기
    while(index > 0 and value < n-1):
        index -= 1;
        value += 1;
    return right_diagonal_used[index][value];



def checkLeftDiagonal(index, value):
    # 왼쪽 위끝에 있는 행/열 찾기
    while (index > 0 and value > 0):
        index -= 1;
        value -= 1;
    return left_diagonal_used[index][value];



def checkPromise(index):
    global n;

    if col_used[col[index]]: #행 검사
        return False;
    elif checkLeftDiagonal(index, col[index]):
        return False;
    elif checkRightDiagonal(index, col[index]):
        return False;

    return True;









# === main function ===#


n = int(input()); #n 크기 입력
col = [None for _ in range(n)];
col_used = [False for _ in range(n)]; #사용한 행 저장
left_diagonal_used = [[False for _ in range(n)] for _ in range(n)]; #왼쪽 위를 향하는 대각선 저장
right_diagonal_used = [[False for _ in range(n)] for _ in range(n)]; #오른쪽 위를 향하는 대각선 저장
result = 0;

queens(0);
print(result);
