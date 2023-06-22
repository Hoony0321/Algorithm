#programmers_12948 - 핸드폰 번호 가리기 (난이도 1)

def solution(phone_number):
    answer = ''
    return ("*" * (len(phone_number) - 4)) + phone_number[-4:]