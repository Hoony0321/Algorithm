#Heap Sort

# heap 정렬 구성 -> root에서 하나 빼고(마지막 원소 root로) -> heap 회복(shift down) -> 반복

#version heap sort => 데이터 하나씩 추가하면서 힙 정렬
def shiftup(heap,idx):
    current = idx;
    spotFound = False;

    while(current > 1 and not spotFound):
        parent = int(current / 2);
        if(heap[current] > heap[parent]):
            # parent와 current 위치 바꾸기;
            heap[current], heap[parent] = heap[parent], heap[current];
            current = parent;
        else: spotFound = True;

def findLargerChild(heap, parent):
    leftIdx = parent * 2; left_child = -1;
    rightIdx = parent * 2 +1; right_child = -1;
    if(leftIdx < len(heap)):
        left_child = heap[parent * 2];
    if(rightIdx < len(heap)):
        right_child = heap[parent * 2 + 1];

    if(left_child == -1 and right_child == -1): return False;

    return leftIdx if left_child > right_child else rightIdx;

def shiftdown(heap,idx):
    parent = idx;
    largerChildIdx = findLargerChild(heap, parent);

    while(largerChildIdx):
        if heap[parent] < heap[largerChildIdx] : #교환
            heap[largerChildIdx], heap[parent] = heap[parent],heap[largerChildIdx]
            parent = largerChildIdx;
            largerChildIdx = findLargerChild(heap, parent); #largerChildIdx 새로 구하기
        else: break;


#============ HEAP SORT 첫번째 방법 ============#
def makeheapVersion1(heap ,data):
    #원소 하나씩 맨 끝에 추가해서 shift up으로 힙 구성
    for elem in data:
        heap.append(elem);
        shiftup(heap,len(heap) -1);

#============ HEAP SORT 두번째 방법 ============#
def makeheapVersion2(heap, data):
    # 모든 데이터를 트리에 넣은상태에서 힙 구성
    for elem in data:
        heap.append(elem);
    startIdx = int((len(heap) - 1) / 2);
    for i in range(startIdx, 0, -1): #floor(원소개수 / 2) 부터 1까지 진행
        shiftdown(heap,i);


def popRoot(heap):
    n = len(heap) - 1;
    heap[0] , heap[n] = heap[n], heap[0];
    return heap.pop(n);

def heapSort(data):
    heap1 = [0]; #계산의 편의를 위해 0번 index 자리 채워놓기 -> 1번 인덱스부터 시작
    result1 = [];

    #데이터 하나씩 넣을때마다 heap sort
    makeheapVersion1(heap1, data);

    for i in range(1,len(heap1)):
        result1.append(popRoot(heap1));
        shiftdown(heap1,0); #다시 힙 구성

    heap2 = [0];  # 계산의 편의를 위해 0번 index 자리 채워놓기 -> 1번 인덱스부터 시작
    result2 = [];

    #데이터 한번에 넣고 heap sort
    makeheapVersion2(heap2, data);
    print(heap2);

    for i in range(1,len(heap2)):
        result2.append(popRoot(heap2));
        shiftdown(heap2,0); #다시 힙 구성

    return [result1[1:] ,result2[1:]];

# data = [17,3,5,1,9,7,21,2,10,4,15,6,11,14]; #임시로 설정
data = [11,14,2,7,6,3,9,5] #실습 교재 슬라이드 예시 데이터
result = heapSort(data);
print(" HEAP SORT VERSION 1 : {}".format(result[0]));
print(" HEAP SORT VERSION 2 : {}".format(result[1]));