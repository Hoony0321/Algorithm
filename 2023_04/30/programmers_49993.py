#문제설명
#programmers_49993 - 스킬트리 (난이도 2)

def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        indexs = []
        for char in skill:
            indexs.append(skill_tree.find(char))
        
        
        #뒤에부터 -1 제거하기.
        while indexs:
            if(indexs[-1] == -1):
                del indexs[-1]
            else:
                break
                
        if(len(indexs)) == 0:
            answer += 1
            continue
            
        prev = -1
        isAvailable = True
        for index in indexs:
            if(index <= prev):
                isAvailable = False
                break
            else:
                prev = index
        
        if(isAvailable): 
            answer += 1
            
            
    return answer