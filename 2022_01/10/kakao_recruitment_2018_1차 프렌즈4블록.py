#kakao_recruitment_2018_1차 프렌즈4블록
def FindBlockSet(m,n,board,removeBoard):
    dxy = [[0,1],[1,0],[1,1]];
    target = None; #기준 블럭
    for row in range(0,m-1): #0부터 m-2까지
        for col in range(0,n-1): #0부터 n-2까지
            target = board[row][col];
            if target == " ": target = None;
            available = True;
            
            for i in range(3):
                nextY = row + dxy[i][0]; nextX = col + dxy[i][1];
                if board[nextY][nextX] != target: #다른 블럭일 경우
                    available = False; break;
            
            if available: #2*2 세트 만족
                removeBoard[row][col] = True;
                for i in range(3):
                    nextY = row + dxy[i][0]; nextX = col + dxy[i][1];
                    removeBoard[nextY][nextX] = True;

def RemoveBlockSet(m,n,board,removeBoard):
    remove = 0;
    for row in range(m):
        for col in range(n):
            if removeBoard[row][col]:
                remove += 1;
                board[row][col] = " ";
    return remove;

def FillTheBlank(m,n,board):
    for col in range(0,n): #0부터 n-1까지
        bottom = None;
        for row in range(m-1,-1,-1): #m-1부터 0까지
            if board[row][col] == " ":
                if bottom == None:
                  bottom = row;
            else:
                if bottom != None:
                    board[bottom][col] = board[row][col];
                    board[row][col] = " ";
                    bottom -= 1;
            
                    
                    
                
    
def solution(m, n, board):
    answer = 0;
    removeBlocks = -1;

    for i in range(m):
      board[i] = list(board[i]);
    
    while removeBlocks != 0:
        removeBoard = [[False for _ in range(n)] for _ in range(m)];
        #2*2 블럭 세트 찾기
        FindBlockSet(m,n,board,removeBoard);

        #찾은 2*2 블럭 세트 지우기
        removeBlocks = RemoveBlockSet(m,n,board,removeBoard);
        answer += removeBlocks;

        #빈 공간 채우기
        FillTheBlank(m,n,board);


    
    return answer
  

print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]));