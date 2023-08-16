def solution(babbling):
    answer = 0
    
    speakWords = ['aya', 'ye', 'woo', 'ma']
    
    for word in babbling:
        
        for speak in speakWords:
            if (speak in word) and (speak*2 not in word):
                word = word.replace(speak, '@')
        if word in '@' * 30:
            answer += 1
        
    
    return answer