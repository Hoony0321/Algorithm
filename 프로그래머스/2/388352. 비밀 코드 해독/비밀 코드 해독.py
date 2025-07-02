def solution(n, q, ans):
    def combination(arr, r):
        result = []
        
        def backtrack(start, path):
            if len(path) == r:
                result.append(path)
                return
            
            for i in range(start, len(arr)):
                path.append(arr[i])
                backtrack(i+1, path[:])
                path.pop()
                
        backtrack(0,[])
        return result
    
    def is_available(arr, query, answer):
        arr_set = set(arr)
        count = 0
        
        for num in query:
            if num in arr_set:
                count += 1
        
        return True if count == answer else False
        
        
        
    
    available_set = combination([i for i in range(1,n+1)], 5)
    
    answer = 0
    for num_set in available_set:
        flag = True
        for i in range(len(q)):
            if not is_available(num_set,q[i],ans[i]):
                flag = False
        
        if flag:
            answer += 1
            

    return answer