#knapsack 알고리즘
#목표 : 가방에 최대한 많은 무게 물건 넣기.
from collections import deque

print('*' * 30 , '너비우선 knapsack', '*' * 30);

class Node:
    def __init__(self, level, weight, profit, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.include = include

    def __repr__(self):
        str1 = "level : {} , weight : {}, profit : {}".format(self.level, self.weight, self.profit);
        return str1;

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



def knapsack_bfs():
    global  bestSet, W, num_items;
    queue = deque();
    maxprofit = 0;




    v = Node(-1,0,0,[False for _ in range(num_items)]);
    num_node = 1;

    queue.append(v);
    max_queueSize = 1;
    print(v);
    while(queue):
        v = queue.popleft();


        # 왼쪽 가지 ( 해당 아이템 포함 )
        num_node += 1;
        u_left = Node( #자식 노드 생성
            v.level + 1,
            v.weight + weightList[v.level + 1],
            v.profit + profitList[v.level + 1],
            v.include[:])
        u_left.include[u_left.level] = True
        if(u_left.weight <= W and u_left.profit > maxprofit): #해당 weight가 maxprofit보다 큰 경우
            maxprofit = u_left.profit;
            bestSet = u_left.include[:];
        if(u_left.weight < W and bound(u_left) > maxprofit): # 유망한 노드임 -> 자식 탐색
            queue.append(u_left);
        print(u_left)
        # 오른쪽 가지 ( 해당 아이템 포함X )
        num_node +=1;
        u_right = Node( #자식 노드 생성
            v.level + 1,
            v.weight,
            v.profit,
            v.include[:])
        if (u_right.weight < W and bound(u_right) > maxprofit):  # 유망한 노드임 -> 자식 탐색
            queue.append(u_right);
        print(u_right)

        if(len(queue) > max_queueSize): max_queueSize = len(queue)

    print("generated node num : {}".format(num_node));
    print("max queue size : {}".format(max_queueSize));
    print("bestProfit : {} ".format(maxprofit))


profitList = [30,28,18,20]
weightList = [3,4,3,5]
num_items = len(profitList);
bestSet= [];
W = 6;



knapsack_bfs();

print("bestSet Index : ", end='');
for i in range(num_items):
    if(bestSet[i]):
        print(i , end=' ');
print();