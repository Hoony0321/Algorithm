#baekjoon_14719_빗물

def isRainField(y,x):
    global W, result;
    if board[y][x] != 0: return; #빈 공간이 아님.

    #왼쪽 확인
    possible = False;
    for nx in range(x,-1,-1): #x부터 0까지 확인
        if board[y][nx] == 1 or board[y][nx] == 2:
            possible = True;
            break;

    if not possible : return;

    #오른쪽 확인
    possible = False;
    for nx in range(x, W):  # x부터 W-1까지 확인
        if board[y][nx] == 1 or board[y][nx] == 2:
            possible = True;
            break;

    if not possible: return;

    board[y][x] = 2;
    result += 1;
    return;

H,W = map(int,input().split());

board = [[0] * W for _ in range(H)];

H_info = list(map(int,input().split()));
result = 0;
for i in range(W):
    height = H_info[i];
    for j in range(1,height+1):
        board[-j][i] = 1; #빗물 표시

for i in range(H):
    for j in range(W):
        isRainField(i,j);

print(result);

