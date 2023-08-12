def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    user_info_dict = {key: [[],0,idx] for idx,key in enumerate(id_list)}
    print(user_info_dict)
    
    for re in set(report):
        reporter, target = re.split(" ")
        user_info_dict[target][0].append(reporter)
        user_info_dict[target][1] += 1
        
    for key,(mail_list, count, _) in user_info_dict.items():
        if(count >= k):
            for user in mail_list:
                answer[user_info_dict[user][2]] += 1
    
    return answer