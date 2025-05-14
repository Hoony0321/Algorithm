from collections import defaultdict
def solution(phone_book):
    answer = True
    
    for i in range(1,20):
        phone_dict = defaultdict(int)
        check_array = []
        for phone in phone_book:
            if len(phone) < i: continue
            if len(phone) == i :
                check_array.append(phone)
            phone_dict[phone[0:i]] += 1
       
        for check_phone in check_array:
            if phone_dict[check_phone] > 1:
                return False
    
            
    return True