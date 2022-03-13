#baekjoon_1039_교환

# === import module ===#
import collections
# === variable declare ===#

# === Function define ===#
def numSwap(number,idx1,idx2):

    number = list(str(number));
    tmp = number[idx1];
    number[idx1] = number[idx2];
    number[idx2] = tmp;

    if number[0] == '0':
        return -1;

    return int("".join(number));



def BFS(N,K):
    queue = collections.deque()
    queue.append([N,0]);
    M = len(str(N));
    max_result = -1;
    while queue:
        number, action = queue.popleft();

        if action == K: #모든 교환 완료
            max_result = max(max_result, number);
            continue;

        for idx1 in range(0,M-1):
            for idx2 in range(idx1+1,M):
                tmpNumber = numSwap(number,idx1,idx2);
                if tmpNumber == -1:
                    continue;
                queue.append([tmpNumber,action+1]);

    return max_result;

# === main function ===#
N,K = map(int,input().split());
max_result = 0;
print(BFS(N,K));



