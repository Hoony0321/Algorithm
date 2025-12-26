def solution(s):
    answer = []
    for string in s:
        stack = []
        count_110 = 0
        
        # 1. 스택을 이용해 모든 "110" 추출
        for char in string:
            if len(stack) >= 2 and stack[-2] == '1' and stack[-1] == '1' and char == '0':
                stack.pop()
                stack.pop()
                count_110 += 1
            else:
                stack.append(char)
        
        # 2. 남은 문자열에서 "110"이 들어갈 위치 찾기
        # 뒤에서부터 처음 나오는 '0'을 찾음
        remaining = "".join(stack)
        idx = remaining.rfind('0')
        
        # 3. '0' 뒤에 "110"들을 이어 붙임 (없으면 맨 앞에 붙임)
        if idx == -1:
            res = "110" * count_110 + remaining
        else:
            res = remaining[:idx+1] + "110" * count_110 + remaining[idx+1:]
        
        answer.append(res)
            
    return answer