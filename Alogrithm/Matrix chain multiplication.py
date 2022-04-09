#연쇄행렬 최소곱셈 알고리즘

n = 7 #행렬 개수
d = [3,5,4,6,7,2,3,4] #행렬 길이 배열
M = [[float('INF') for _ in range(n+1)] for _ in range(n+1)]
P = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    M[i][i] = 0;



def printMatrix(matrix):
    global n
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(matrix[i][j], end=' ');
        print();

def minmult(n , d):

    for diagonal in range(1,n): #1부터 n-1까지
        for i in range(1, n - diagonal +1): #1부터 n-diagonal까지
            j = i + diagonal;
            for k in range(i,j): # i부터 j-1까지
                originVal = M[i][j];
                M[i][j] = min(M[i][j] , M[i][k] + M[k+1][j] + (d[i-1] * d[k] * d[j])) #최소값 구하기
                if M[i][j] != originVal: #값이 변경됨.
                    P[i][j] = k;

    return M[1][n];

def order(i,j):
    if(i == j):
        print("A{}".format(i), end='')
    else:
        k = P[i][j];
        print("(",end='')
        order(i,k)
        order(k+1,j);
        print(")",end='')


print(minmult(n,d))
print("="*15 + "Matrix 곱셈 정보" + "="*15)
printMatrix(M)
print("="*15 + "Path 정보" + "="*15)
printMatrix(P)
print("="*15 + "Order 정보" + "="*15)
order(1,n)



