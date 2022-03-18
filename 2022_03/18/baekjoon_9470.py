#baekjoon_9470_Strahler순서
from collections import deque

T = int(input()); #테스트 개수

for _ in range(T):
    K,M,P = map(int,input().split());

    graph = [[None for _ in range(M+1)] for _ in range(M+1)];
    childInfo = [[] for _ in range(M+1)];
    orderList = [[] for _ in range(M+1)];
    for _ in range(P):
        fromNode, toNode= map(int,input().split());

        graph[fromNode][toNode] = 1;
        childInfo[toNode].append(fromNode);

    queue = deque();
    for i in range(1,M+1):
        if len(childInfo[i]) == 0: #강의 근원
            orderList[i] = 1;
            queue.append(i);

    while queue:
        curNode = queue.popleft();
        for nextNode in range(1,M+1):
            if graph[curNode][nextNode] != 1: continue; #해당 간선 존재하지 않음
            #print(curNode,nextNode);
            orderList[nextNode].append(orderList[curNode]);

            if len(childInfo[nextNode]) == len(orderList[nextNode]): #자신한테 들어오는 강의 순서 다 받음.
                max_order = 0;
                count = 0;
                for j in range(len(orderList[nextNode])):
                    if orderList[nextNode][j] > max_order:
                        max_order = orderList[nextNode][j];
                        count = 1;
                    elif orderList[nextNode][j] == max_order:
                        count += 1;

                #order 확정
                if count >= 2:
                    orderList[nextNode] = max_order+1;
                else:
                    orderList[nextNode] = max_order;

                queue.append(nextNode);

    print(K,orderList[-1]);










