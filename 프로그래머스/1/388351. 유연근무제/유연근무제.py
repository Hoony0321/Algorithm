def solution(schedules, timelogs, startday):
    def get_max_work_start_time(time):
        h = time // 100
        m = time % 100
        m += 10
        if m >= 60:
            h += 1
            m -= 60
        return h * 100 + m

    n = len(schedules)
    answer = n

    for i in range(n):
        max_work_start_time = get_max_work_start_time(schedules[i])

        for j in range(7):
            weekday = (j + startday) % 7
            if weekday == 6 or weekday == 0:  # 토요일(6), 일요일(0) 제외
                continue

            if timelogs[i][j] > max_work_start_time:
                answer -= 1
                break

    return answer