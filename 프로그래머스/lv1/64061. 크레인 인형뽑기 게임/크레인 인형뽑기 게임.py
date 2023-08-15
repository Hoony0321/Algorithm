def solution(board, moves):
    answer = 0
    stack = []
    board_zip = [list(item) for item in list(zip(*board))]
    
    for move in moves:
        for idx, fig in enumerate(list(board_zip[move-1])):
            if(fig != 0):
                stack.append(fig)
                board_zip[move-1][idx] = 0
                        
                if(len(stack) > 1 and stack[-1] == stack[-2]):
                    answer += 2
                    stack = stack[:-2]
                
                break
    
    
    
    return answer