#이분검색 알고리즘
import random

def binarySearch(x, S):
    low = 0;
    high = len(S) - 1;

    searchNum = 0;  # 탐색 횟수
    while (low <= high): #low가 high보다 커지면 빠져나옴.
        searchNum += 1;
        mid = (low + high) // 2;

        if S[mid] == x:  # 값 찾음. 종료.
            break;

        elif S[mid] < x:  # 찾고자 하는 값보다 작음. 오른쪽 탐색
            low = mid + 1;

        elif S[mid] > x:  # 찾고자 하는 값보다 큼. 왼쪽 탐색
            high = mid - 1;

    return searchNum;  # 탐색 횟수 반환


n = int(input()); #입력 데이터 크기 (128,256,512)

searchNumTotal = 0;
for p in range(1000): #총 1000번의 테스트 케이스 진행
    dataSet = [random.randrange(1, n + 1) for _ in range(n)];  # 1부터 n사이의 정수 난수 n번 발생.
    dataSet.sort(); #비내림차순 정렬
    x = random.randrange(1,n+1); #1부터 n사이의 임의 정수 발생
    searchNumTotal += binarySearch(x,dataSet);


print(searchNumTotal/1000);




