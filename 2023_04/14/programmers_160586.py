#문제정보
#programmers_160586 - 연습문제 - 대충만든자판 (난이도1)

def solution(keymap, targets):
    answer = []
    
    keyCountDictionary = {}
    
    for keyInfo in keymap:
        for idx, char in enumerate(keyInfo):
            if(char in keyCountDictionary):
                if(keyCountDictionary[char] > idx + 1):
                    keyCountDictionary[char] = idx+1
            else:
                keyCountDictionary[char] = idx + 1
    
    
    for target in targets:
        count = 0
        for key in target:
            if key in keyCountDictionary:
                count += keyCountDictionary[key]
            else:
                count = -1
                break
        
        answer.append(count)
            
        
    
    return answer