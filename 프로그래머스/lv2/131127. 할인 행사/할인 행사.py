def solution(want, number, discount):
    answer = 0
    dict_discount = dict()
    
    for item in set(discount):
        dict_discount[item] = 0
    
    for item in discount[0:10]:
        dict_discount[item] += 1

    
    day = 0
    while(day <= len(discount)-10):
        isFind = True
        for i in range(len(want)):
            try :
                if dict_discount[want[i]] != number[i]:
                    isFind = False
                    break
            except KeyError:
                return 0
        
        if(isFind):
            answer += 1
        
        if(day != len(discount)-10):
            dict_discount[discount[day]] -= 1
            dict_discount[discount[day+10]] += 1
        
        day += 1
    
    return answer