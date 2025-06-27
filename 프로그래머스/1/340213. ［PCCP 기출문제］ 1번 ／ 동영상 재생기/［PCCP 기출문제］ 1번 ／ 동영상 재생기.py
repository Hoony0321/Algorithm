def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    def format_time(time):
        if isinstance(time, str):
            arr = time.split(":")
            return int(arr[0]) * 60 + int(arr[1])
        elif isinstance(time, int):
            hours = time // 60
            minutes = time % 60
            return f"{hours:02d}:{minutes:02d}"
    
    
    def prev():
        return pos - 10 if pos - 10 >= 0 else 0
    
    def next():
        return pos + 10 if pos + 10 <= video_len else video_len
    
    def skip():
        if op_start <= pos <= op_end:
            return op_end
        else:
            return pos
        
        
    
    video_len, pos, op_start, op_end = format_time(video_len), format_time(pos), format_time(op_start), format_time(op_end)
    
    for command in commands:
        pos = skip()
        
        if command == "prev":
            pos = prev()
        
        if command == "next":
            pos = next()
            

        print(format_time(pos))
        
    pos = skip()
    return format_time(pos)