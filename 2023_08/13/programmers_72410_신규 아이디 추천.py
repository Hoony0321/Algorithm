import re
def solution(new_id):
    answer = ''
    
    #1단계
    new_id = new_id.lower()
    
    #2단계
    allowedCharList = [chr(i) for i in range(97,123)] + [str(i) for i in range(0,10)] + ['-'] + ['_'] + ['.']
    tmp_new_id = ""
    for char in new_id:
        if char in allowedCharList:
            tmp_new_id += char
    new_id = tmp_new_id
    
    #3단계
    new_id = re.sub(r'\.{2,}', '.', new_id)
    
    #4단계
    if(len(new_id) <= 1):
        if(len(new_id) == 1):
            if(new_id[0] == '.'):
                new_id = ''
    else:
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    #5단계
    if(len(new_id) == 0):
        new_id = 'a'
    
    #6단계
    if(len(new_id) >= 16):
        new_id = new_id[:15]
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    #7단계
    if(len(new_id) <= 2):
        new_id += new_id[-1] * (3 - len(new_id))
        
    answer = new_id
    return answer