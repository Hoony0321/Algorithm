def solution(n, info):
    answer = [-1]
    
    def get_winner(lion, apeach):
        lion_score = 0
        apeach_score = 0
        for i in range(0,11):
            if lion[i] == 0 and apeach[i] == 0:
                continue
            if lion[i] > apeach[i]:
                lion_score += 10 - i
            elif lion[i] <= apeach[i]:
                apeach_score += 10 - i
        
        score_diff = lion_score - apeach_score
        
        return ["lion",score_diff] if lion_score > apeach_score else ["apeach",score_diff]
    
    def show_all_cases(n,r):
        result = []
        case = [0] * n
        
        def backtrack(depth,start):
            if depth == r:
                result.append(tuple(case))
                return
            
            for i in range(start,-1,-1):
                case[i] += 1
                backtrack(depth+1,i)
                case[i] -= 1
        
        backtrack(0,n-1)
        return result
        
    
    result = show_all_cases(11,n)
    max_score_diff = 0
    for case in result:
        winner, score_diff = get_winner(case, info)
        if winner == "lion" and score_diff > max_score_diff:
            max_score_diff = score_diff
            answer = case
    
    return answer