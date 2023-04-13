def solution(name, yearning, photo):
    answer = []
    
    score = dict(zip(name,yearning))
    
    def getScore(image):
        sum = 0
        for name in image:
            if name in score:
                sum += score[name] 
        return sum
    
    for image in photo:
        answer.append(getScore(image)) 
    
    return answer