<<<<<<< Updated upstream
A = [1,2,3,4,5,6,7,8,9];

A[1],A[3] = A[3],A[1];

print(A);
=======
import sys

n = 7 #행렬 개수
d = [3,5,4,6,7,2,3,4] #행렬 길이 배열
M = [[float('INF') for _ in range(n+1)] for _ in range(n+1)]

for diag in range(1, n+1):
    for i in range(1, n+1 - diag):
        j = i + diag
        M[i][j] = sys.maxsize
        for k in range(i, j):
            M[i][j] = min(M[i][j],
                          M[i][k] + M[k + 1][j] + d[i - 1] * d[k] * d[j])

print(M[1][n])
>>>>>>> Stashed changes
