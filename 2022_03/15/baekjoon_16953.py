#baekjoon_16953_A->B
from collections import deque

def BFS(A,B):
    queue = deque();
    queue.append(A);
    success = False;

    action = 0;
    while queue and not success:

        for _ in range(len(queue)):
            num = queue.popleft();

            if num > B: #수를 초과함.
                continue;
            elif num == B: #정답
                success = True;
                break;
            else: #계속 진행
                #2곱하기
                queue.append(num *2);
                #오른쪽에 1 추가
                tmpNum = str(num);
                tmpNum += '1';
                queue.append(int(tmpNum));

        action += 1;

    if success:
        return action;
    else:
        return -1;



A , B = map(int,input().split());

print(BFS(A,B));




