def solution(phone_book):
    phone_dict = dict()
    for phone in phone_book:
        phone_dict[phone] = True
    
    for phone in phone_book:
        for i in range(1,len(phone)):
            try:
                if(phone_dict[phone[:i]]): return False
            except KeyError:
                pass
        
    return True