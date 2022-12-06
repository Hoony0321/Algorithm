
n,m = map(int,input().split());

def turn_off_matrix(y,x):
    for i in range(y,y+3):
        for j in range(x,x+3):
            mat1[i][j] = 0 if (mat1[i][j]) == 1 else 1

def check_equal_matrix():
    return mat1 == mat2

#첫번째 행렬
mat1 = []
for i in range(n):
    row = input()
    mat1.append([int(i) for i in row])

#두번째 행렬
mat2 = []
for i in range(n):
    row = input()
    mat2.append([int(i) for i in row])

number = 3
x_times = m - number + 1
y_times = n - number + 1


if check_equal_matrix():
    print(0)
    exit(0)

if x_times < 0 or y_times < 0: 
    print(-1) 
    exit(0)





is_equal_matrix = False
turn_times = 0
for i in range(y_times):
    if(is_equal_matrix): break    
    for j in range(x_times):
        if mat1[i][j] != mat2[i][j]:
            turn_off_matrix(i,j)
            turn_times += 1
        is_equal_matrix = check_equal_matrix()
        if(is_equal_matrix): break

print(turn_times if is_equal_matrix else -1)