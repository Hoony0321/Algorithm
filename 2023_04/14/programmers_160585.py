def solution(board):
    answer = -1
    
    # 게임이 종료된 상태인지 판단
    winnerList = []
    winInfo = []
    for i in range(len(board)): #check row
        if board[i][0] == board[i][1] == board[i][2]:
            if(board[i][0] != "."):
                winnerList.append(board[i][0])
                winInfo.append([[i,0], [i,1], [i,2]])
    
    for j in range(len(board)): #check column
        if board[0][j] == board[1][j] == board[2][j]:
            if(board[i][0] != "."):
                winnerList.append(board[0][j])
                winInfo.append([[0,j], [1,j], [2,j]])
    
    #check diagonal
    if board[0][0] == board[1][1] == board[2][2]:
            if(board[i][0] != "."):
                winnerList.append(board[0][0])
                winInfo.append([[0,0], [1,1], [2,2]])
        
    if board[0][2] == board[1][1] == board[2][0]:
            if(board[i][0] != "."):
                winnerList.append(board[0][2])
                winInfo.append([[0,2], [1,1], [2,0]])
    
    if(len(winnerList) > 2): return 0
    elif(len(winnerList) == 2):
        if(winnerList[0] != winnerList[1]): return 0
        winInfo1, winInfo2 = winInfo[0], winInfo[1]
        isCan = False
        for elem in winInfo1:
            if elem in winInfo2:
                isCan = True
                break
        if(not isCan): return 0
    else:
        if(len(winnerList) == 1): winner = winnerList[0]
        else: winner = "."
    
    # 현재 게임이 순서를 맞게 지켜서 했는지 판단
    countO = 0
    countX = 0
    for row in board:
        for char in row:
            if(char == "O"): countO += 1
            elif(char == "X"): countX += 1
    
    if(countX > countO or countO - countX > 1): answer=0 #진행 순서가 이상한 경우
    if(winner == "X" and countO != countX ): answer=0 #게임이 끝났는게 O가 계속 진행한 경우
    if(winner == "O" and countO == countX): answer=0 #게임이 끝났는데 X가 계속 진행한 경우
    
    if((countO+countX) % 2 == 0 and countO != countX):answer=0
    if((countO+countX) % 2 != 0 and countO-countX != 1): answer=0
    
    if(answer == -1): answer = 1
    return answer