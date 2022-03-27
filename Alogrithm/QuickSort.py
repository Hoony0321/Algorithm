#QuickSort 구현
import random



def Partition(low, high, pivotpoint):
    global sum_of_operation;
    pivotitem = dataSet[low];
    j = low;
    for i in range(low + 1, high+1): #low부터 high까지
        if dataSet[i] < pivotitem:  # pivotItem 보다 작은 아이템 왼쪽으로 정렬 - 단위 연산
            sum_of_operation += 1; #단위연산 증가
            j += 1;
            dataSet[i], dataSet[j] = dataSet[j], dataSet[i];

    pivotpoint[0] = j;
    dataSet[low], dataSet[pivotpoint[0]] = dataSet[pivotpoint[0]], dataSet[low];


def QuickSort(low, high):
    pivotpoint = [None];
    if (high > low):
        Partition(low, high, pivotpoint);
        QuickSort(low, pivotpoint[0] - 1);
        QuickSort(pivotpoint[0] + 1, high);


sum_of_operation = 0; #단위 연산 횟수 합
n = int(input()); #데이터 크기 입력

for _ in range(100): #100개의 테스트 케이스 실행
    dataSet = [random.randrange(0, n + 1) for _ in range(n)];  # 0부터 n까지 랜덤 정수 n개 생성
    QuickSort(0,len(dataSet)-1);

print(sum_of_operation / 100); #평균 비교 횟수

# n = 100 -> 300.75
# n = 200 -> 723.221
# n = 300 -> 1206.49
# n = 400 -> 1767.01




