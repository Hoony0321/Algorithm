#문제설명
#programmers_131701 - 연속 부분 수열 합의 개수 (난이도 2)

def solution(elements):
    answer = set()
    for length in range(len(elements)-1): #길이가 최대인 원소 제외
        for start in range(len(elements)):
            newElement = -1
            end = start + length
            if(end > len(elements)-1): #마지막 원소가 범위 초과 (queue 맨 처음으로 돌아가기)
                arr1 = elements[start:end]
                arr2 = elements[0:end - len(elements)+1]
                newElement = sum(arr1) + sum(arr2)
            else:
                newElement = sum(elements[start:end+1])
            
            answer.add(newElement)
            
    
    answer.add(sum(elements)) #길이가 최대인 원소 경우 추가
    
    return len(answer)
