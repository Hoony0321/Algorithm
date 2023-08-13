def find_position(target):
    keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    for i, row in enumerate(keypad):
        for j, val in enumerate(row):
            if val == target:
                return [i, j]
        

def solution(numbers, hand):
    answer = ""
    lPos, rPos = '*', '#'
    
    leftSide = [1,4,7]
    rightSide = [3,6,9]
    
    
    for number in numbers:
        if number in leftSide:
            lPos = number
            answer += 'L'
        elif number in rightSide:
            rPos = number
            answer += 'R'
        else:
            lKeyPadPos = find_position(lPos)
            rKeyPadPos = find_position(rPos)
            targetKeyPadPos = find_position(number)
            
            lDiff = abs(lKeyPadPos[0] - targetKeyPadPos[0]) + abs(lKeyPadPos[1] - targetKeyPadPos[1])        
            rDiff = abs(rKeyPadPos[0] - targetKeyPadPos[0]) + abs(rKeyPadPos[1] - targetKeyPadPos[1])        
            if lDiff < rDiff:
                lPos = number
                answer += 'L'
            elif rDiff < lDiff:
                rPos = number
                answer += 'R'
            else:
                if(hand == 'left'):
                    lPos = number
                    answer += 'L'
                else:
                    rPos = number
                    answer += 'R'
    
    return answer