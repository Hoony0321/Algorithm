#문제정보
#programmers_77885 - 연습문제 - 2개 이하로 다른 비트 (난이도2)

def solution(numbers):
    answer = []
    
    for number in numbers:
        if number % 2 == 0: #짝수일때
            answer.append(number+1)
        else: #홀수일때
            binNumber = str(bin(number)).replace('b','')
            
            rIndex = len(binNumber) - 1 - binNumber.rfind('0')
            answer.append(number + 2 ** rIndex - 2 ** (rIndex-1))
    
            
            
    
    return answer