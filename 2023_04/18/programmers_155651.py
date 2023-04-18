#문제 정보
#programmers_155651 - 호텔 대실 (난이도 2)

def timeToMin(time):
    hour, minute = map(int, time.split(":"))
    return hour * 60 + minute

def solution(book_time):
    rooms = []
    
    for index, times in enumerate(book_time):
        start,end = timeToMin(times[0]), timeToMin(times[1])
        book_time[index] = [start,end]
    
    book_time.sort(key=lambda x : x[0])
    
    
    for times in book_time:
        start,end = times
        
        isEnter = False
        for index, room in enumerate(rooms):
            if(room > start): continue
            isEnter = True
            rooms[index] = end + 10
            break
        
        if(not isEnter):
            rooms.append(end + 10)
        
    
    
    return len(rooms)