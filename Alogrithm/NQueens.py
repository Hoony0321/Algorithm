#N-Queens problem Algorithm

def queens(index):
    global n, result, pre_tree_num, post_tree_num;


    if(index == n): #마지막 단계이면 result 출력
        print(col);
        result += 1;
    else: #마지막 단계아님.
        for value in range(0,n):
            post_tree_num += 1;
            col[index] = value;
            promising = checkPromise(index); #유망성 검사.
            if promising:
                queens(index+1); #다음 단계로 진행
                pre_tree_num += 1;



def checkPromise(index):
    promising = True;

    for pre_index in range(0, index):  # 이전에 들어간 값들과 비교하면서 검사
        if (col[index] == col[pre_index] or  # 같은 열인지 검사
                abs(index - pre_index) == abs(col[index] - col[pre_index])):  # 같은 대각선에 있는지 검사
            promising = False; break; #유망한 노드 아님. 가지치기!

    return promising;



#n = int(input()); #n 크기 입력
n = 7;
col = [None for _ in range(n)];
result = 0;
pre_tree_num = 0;
post_tree_num = 0;

print("=" * 10 , " 가능한 모든 경우 ", "=" * 10);
queens(0);
print("=" * 10 , " 가한 모든 경우의 수 ", "=" * 10);
print(result);

print("=" * 10 , "Node 생성 후 Promising 검사할 때 생성되는 Node 수 ", "=" * 10);
print(post_tree_num);

print("=" * 10 , "Promising 검사를하고 Node 생성할 때 생성되는 Node 수 ", "=" * 10);
print(pre_tree_num);