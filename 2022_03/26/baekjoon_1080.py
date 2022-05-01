n, m = map(int, input().split())
graph1 = []
graph2 = []
count = 0

def convertgraph(i, j):			# 3x3을 뒤집는 함수
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            graph1[x][y] = 1 - graph1[x][y]


for i in range(n):				# 변환 전 함수 입력
    graph1.append(list(map(int, input())))

for i in range(n):				# 변환 후 함수 입력
    graph2.append(list(map(int, input())))

for i in range(n - 2):
    for j in range(m - 2):
        if graph1[i][j] != graph2[i][j]: # 일치하지 않는 부분 발생
            convertgraph(i, j)			 # 뒤집고
            count += 1				 	 # 횟수 + 1
flag = 0							# 변환 할 수 있는지 나타내는 변수

for i in range(n):					# 변환 후 일치하는지 확인
    for j in range(m):
        if graph1[i][j] != graph2[i][j]:
            flag = 1
            break

if flag == 1:							# 변환이 불가능 하면 -1 반환
    print(-1)
else:
    print(count)