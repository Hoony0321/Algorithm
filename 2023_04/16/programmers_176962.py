#문제정보
#programmers_176962 - 과제 진행하기 (난이도2)

from collections import deque

def timeToMin(time):
    hour, minute = map(int,time.split(":"))
    return hour * 60 + minute
    
def solution(plans):
    answer = []
    remainHomework = deque()
    curTime = plans
    
    for index in range(len(plans)): #convert time to min
        plans[index][1] = timeToMin(plans[index][1])
        
    plans.sort(key=lambda x:x[1]) #sort by time
    
    for index in range(len(plans)):
        name, curTime, playTime = plans[index]
        playTime = int(playTime)
        
        if(index == len(plans) -1): #마지막 원소일 경우
            answer.append(name)
            for name,remainTime in remainHomework:
                answer.append(name)
            break
        
        nextTime = plans[index+1][1]
        
        if(curTime + playTime > nextTime): #중간에 과제를 그만두고 다음 과제해야 함.
            remainHomework.appendleft([name, playTime - (nextTime - curTime)])
            continue
        else: #현재 과제를 마칠 수 있을때
            answer.append(name)
            curTime += playTime
            ableTime = nextTime - curTime
            
            while(remainHomework and curTime < nextTime):
                ableTime = nextTime - curTime
                name, remainTime = remainHomework[0]
                if(remainTime > ableTime):
                    remainTime -= ableTime
                    remainHomework[0][1] = remainTime
                    break
                else:
                    answer.append(name)
                    curTime += remainTime
                    remainHomework.popleft()
                    continue
            
        
        
    return answer