#DNA 서열 최적 맞춤
def opt(i,j):
    global n,m
    if i == m:
        table[i][j] = 2*(n-j)
        return
    elif j == n:
        table[i][j] = 2*(m-i)
        return
    else:
        if a[i] == b[j]: penalty = 0
        else: penalty = 1
        table[i][j] = min(table[i+1][j+1] + penalty, table[i+1][j] + 2, table[i][j+1] + 2)

def findPath(i,j):
    global m,n

    if i >= m or j >= n: return
    penalty = 0 if a[i] == b[j] else 1

    if table[i][j] == table[i][j+1] + 2:
        minindex[i][j] = (i,j+1)
        findPath(i, j + 1) #다음 단계로 진행
    elif minindex[i][j] == table[i+1][j] + 2:
        minindex[i][j] = (i+1,j)
        findPath(i + 1, j) #다음 단계로 진행
    elif table[i][j] == table[i+1][j+1] + penalty:
        minindex[i][j] = (i+1,j+1)
        findPath(i+1,j+1) #다음 단계로 진행




a = ['G','A','C','T','T','A','C','C']
b = ['C','A','C','G','T','C','C','A','C','C']

m = len(a); n = len(b);
table = [[0 for _ in range(n+1)] for _ in range(m+1)]
table[m][n] = 0;
minindex = [[0 for _ in range(n+1)] for _ in range(m+1)]

#양 끝 index table 값 채우기
for j in range(n-1,-1,-1):
    table[m][j] = table[m][j+1] + 2

for i in range(m-1,-1,-1):
    table[i][n] = table[i+1][n] + 2

#테이블 채우기 - 아래부터 차례대로 채우면 됨
for i in range(m-1,-1,-1): #m-1부터 0까지
    for j in range(n-1,-1,-1): #n-1부터 0까지
        opt(i,j)

for row in table:
    for elem in row:
        print("{:5}".format(elem), end=' ')
    print()


#minindex table 채우기
print()
findPath(0,0)

x,y = 0,0
while (x < m and y < n):
    tx, ty = x, y # x와 y는 0부터 시작
    print(minindex[x][y])
    (x,y)= minindex[x][y]
    if x == tx + 1 and y == ty+1:
        print(a[tx]," ",  b[ty])
    elif x == tx and y == ty+1:
        print(" - ", " ", b[ty])
    else:
        print(a[tx], " " , " -")