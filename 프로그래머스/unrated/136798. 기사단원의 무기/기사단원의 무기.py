def getDivisors(number):
    if(number == 1) : return 1
    
    divisors = set()
    
    count = 0
    for i in range(1, int(number ** 0.5)+1):
        if(number % i == 0):
            divisors.add(i)
    
    tmp_divisors = divisors.copy()
    
    for i in tmp_divisors:
        divisors.add(number//i)

    return len(divisors)

def getCost(power, limit, limitPower):
    if(power > limit):
        return limitPower
    
    else:
        return power

            

def solution(number, limit, power):
    answer = 0
    
    divisorCounts = []
    
    for num in range(1, number+1):
        divisorCounts.append(getDivisors(num))
    
    for count in divisorCounts:
        answer += getCost(count,limit,power)
    
    
    
    return answer