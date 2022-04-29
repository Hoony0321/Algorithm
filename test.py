n = int(input());
Matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
P = [[0 for _ in range(n+1)] for _ in range(n+1)]


for diagonal in range(1,n): #1부터 n-1까지
    for i in range(1, n - diagonal +1): #1부터 n - diagonal까지
        j = i + diagonal;

