def solution(X, Y):
    answer = ""
    numDict = {key:0 for key in range(0,10) }
    
    for num in numDict.keys():
        numDict[num] = min(X.count(str(num)), Y.count(str(num)))
    
    for num in range(9,-1,-1):
        if(numDict[num] != 0):
            answer += str(num) * numDict[num]
    
    if(len(answer) > 1 and len(answer) == answer.count("0")):
        answer = "0"
    
    return answer if answer != "" else "-1"