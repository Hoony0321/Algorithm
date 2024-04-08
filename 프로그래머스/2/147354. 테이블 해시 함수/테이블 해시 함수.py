def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x : (x[col-1], -x[0]))
    
    result = -1
    for i in range(row_begin, row_end+1):
        numModSum = 0
        for num in data[i-1]:
            numModSum += num % i
        
        
        if result == -1:
            result = numModSum
        else:
            result = result ^ numModSum
    
    return result