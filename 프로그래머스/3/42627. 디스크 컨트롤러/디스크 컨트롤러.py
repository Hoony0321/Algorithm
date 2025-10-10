import heapq
from collections import deque
def solution(jobs):
    answer = 0
    totalTime = []
    process = None
    queue = []
    jobs.sort(key = lambda x : x[0])
    jobDeque = deque(jobs)
    
    # 소요시간 짧은 것, 작업 요청 시각이 빠른 것, 작업의 번호가 작은 것
    t = -1
    while(jobDeque or queue or process):
        t += 1
        
        # 넣을 수 있는 작업이 있으면 큐에 추가
        while (jobDeque and jobDeque[0][0] <= t):
            reqTime, duration = jobDeque.popleft()
            heapq.heappush(queue, [duration,reqTime])
        
        # process가 있을 경우 진행
        if process != None:
            process -= 1
            if process <= 0:
                process = None
        
        # 진행중인 process가 없을 경우 새로운 작업 할당
        if process == None and queue:
            duration, reqTime = heapq.heappop(queue)
            # 완료 시각 미리 계산해서 저장
            totalTime.append(t + duration - reqTime)
            process = duration
    
    print(totalTime)
    answer = sum(totalTime) // len(totalTime)
        
    
    
    return answer