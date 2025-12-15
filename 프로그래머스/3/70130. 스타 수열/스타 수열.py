def solution(a):
    answer = -1
    
    def getStarSequence(num):
        starSeq = []
        seq = []
        flag = False # num이 들어가있는지 에크
        
        for elem in a:
            if elem == num:
                if len(seq) == 1 and flag:
                    continue
                else:
                    seq.append(elem)
                    flag = True    
            else:
                if len(seq) == 1 and flag:
                    seq.append(elem)
                elif len(seq) == 1 and not flag:
                    continue
                else:
                    seq.append(elem)
            
            if len(seq) == 2:
                starSeq += seq
                flag = False
                seq = []
        
        return starSeq
    
    a_dict = dict()
    for num in a:
        if num in a_dict:
            a_dict[num] += 1
        else:
            a_dict[num] = 1
    
    for num in a_dict.keys():
        if answer >= a_dict[num] * 2:
            continue
        result = getStarSequence(num)
        # print(result)
        answer = max(answer, len(result))
    
    return answer