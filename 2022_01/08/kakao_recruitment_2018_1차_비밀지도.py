#kakao_recruitment_2018_1차 비밀지도

def solution(n, arr1, arr2):
    answer = []
    
    for idx in range(n):
        str = '';
        result = arr1[idx] | arr2[idx];
        for i in range(n-1,-1,-1):
            if result & (1 << i) == 0:
                str += ' ';
            else:
                str += '#';
        
        answer.append(str);
            
            
    
    
    return answer
