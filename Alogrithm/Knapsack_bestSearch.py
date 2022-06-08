#knapsack 알고리즘
#목표 : 가방에 최대한 많은 무게 물건 넣기.
# best-first search 방법 이용 - 가장 좋은 한계치를 가진 node부터 우선 탐색!
# 우선순위 대기열 이용 - maxHeap을 이용하자!
import heapq

class Node:
    def __init__(self, level, weight, profit, include, bound):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.include = include
        self.bound = bound;

    def __repr__(self):
        return "level : {} , weight : {}, profit : {}, bound : {}".format(self.level, self.weight, self.profit, self.bound);


    def __lt__(self, other):
        return self.bound > other.bound #max-heap 조건 비교를 위한 설정

def bound(node):
    global W, num_items

    if node.weight >= W: #남은 공간 없음.
        return node.profit;

    #배낭에 남은 공간이 있을 경우
    boundProfit = node.profit;
    totalWeight = node.weight;

    last = None;
    for i in range(node.level+1, num_items):
        last = i;
        if(totalWeight + weightList[i] > W):
            break;

        totalWeight += weightList[i];
        boundProfit += profitList[i];


    if(totalWeight < W and last < num_items):
        boundProfit += (W - totalWeight) * int(profitList[last]/weightList[last])

    return boundProfit



def knapsack_bestFirst():
    global  bestSet, W, num_items;
    priorityQueue = []
    maxprofit = 0;




    v = Node(-1,0,0,[False for _ in range(num_items)],float('INF'));
    num_node = 1;

    heapq.heappush(priorityQueue, v);
    max_queueSize = 1;

    print(v);
    while(priorityQueue):
        v = heapq.heappop(priorityQueue);


        if(v.bound <= maxprofit): #현재 노드가 아직도 유효한지 확인. 상한이 maxprofit 이하이면 탐색 X
            continue;

        # 왼쪽 가지 ( 해당 아이템 포함 )
        num_node += 1;
        u_left = Node( #자식 노드 생성
            v.level + 1,
            v.weight + weightList[v.level + 1],
            v.profit + profitList[v.level + 1],
            v.include[:], 0)
        u_left.include[u_left.level] = True
        u_left.bound = bound(u_left);

        print(u_left);

        if(u_left.weight <= W and u_left.profit > maxprofit): #해당 weight가 maxprofit보다 큰 경우
            maxprofit = u_left.profit;
            bestSet = u_left.include[:];
        if(u_left.weight < W and u_left.bound > maxprofit): # 유망한 노드임 -> 자식 탐색
            heapq.heappush(priorityQueue,u_left);

        # 오른쪽 가지 ( 해당 아이템 포함X )
        num_node +=1;
        u_right = Node( #자식 노드 생성
            v.level + 1,
            v.weight,
            v.profit,
            v.include[:], 0)
        u_right.include[u_right.level] = False;
        u_right.bound = bound(u_right);

        print(u_right);


        if (u_right.weight < W and u_right.bound > maxprofit):  # 유망한 노드임 -> 자식 탐색
            heapq.heappush(priorityQueue,u_right);

        if(len(priorityQueue) > max_queueSize): max_queueSize = len(priorityQueue)

    print("generated node num : {}".format(num_node));
    print("max queue size : {}".format(max_queueSize));
    print("bestProfit : {} ".format(maxprofit))


profitList = [30,28,18,20]
weightList = [3,4,3,5]
num_items = len(profitList);
bestSet= [];
W = 6;



knapsack_bestFirst();

print("bestSet Index : ", end='');
for i in range(num_items):
    if(bestSet[i]):
        print(i , end=' ');
print();




