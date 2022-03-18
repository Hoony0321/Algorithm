#baekjoon_1700_멀티탭 스케줄링
from collections import deque

N,K = map(int,input().split()); #멀티탭 구멍, 사용 횟수

multiTab = [];
action = 0;

inputList = list(map(int,input().split()));
useOrder = deque(inputList);

for _ in range(len(useOrder)):
    useProd = useOrder.popleft();

    #이미 해당 제품이 꽂혀있는 경우
    if useProd in multiTab: continue;

    #멀티탭에 자리가 있는 경우
    if len(multiTab) < N:
        multiTab.append(useProd);
        continue;

    #멀티탭에 빈 곳이 없는 경우
    else:
        tmpList = multiTab[:];
        for idx in range(len(useOrder)):
            if len(tmpList) == 1: break;
            if useOrder[idx] in tmpList:
                tmpList.remove(useOrder[idx]);

        for num in tmpList:
            multiTab.remove(num);
            action += 1;

        multiTab.append(useProd);#멀티탭에 추가

print(action - (N - len(multiTab)));



