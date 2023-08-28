def solution(record):
    answer = []
    user_name_dict = {}
    admin_message_list = []
    for rec in record:
        data  = rec.split(" ")
        
        if(data[0] == 'Leave'):
            in_out, user_id  = data
        else:
            in_out, user_id, nickname = data
            
        
        # 이름 변경
        if(in_out == 'Enter' or in_out == 'Change'):
            user_name_dict[user_id] = nickname
        
        # 메시지 추가
        if(in_out == 'Change'): continue
        admin_message_list.append([user_id, 0 if in_out == 'Leave' else 1])
    
    for user_id, isEnter in admin_message_list:
        if(isEnter):
            answer.append(f'{user_name_dict[user_id]}님이 들어왔습니다.')
        else:
            answer.append(f'{user_name_dict[user_id]}님이 나갔습니다.')
    
    return answer