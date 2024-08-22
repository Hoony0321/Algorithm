def solution(s):
    answer = []
    tupleList = []
    
    s = s[2:-2].split('},{')
    
    for elem in s:
        tupleList.append(elem.split(","))
    
    tupleList.sort(key=len)

    for tup in tupleList:
        for num in map(int,tup):
            if num not in answer:
                answer.append(num)
                
                
    return answer