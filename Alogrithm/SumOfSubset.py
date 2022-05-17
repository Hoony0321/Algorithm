#부분집합의 합 구하기 알고리즘 (BackTracking)
#논리 전개 순서
# n개의 item 오름차순 정렬
# 첫번째 item부터 포함/미포함으로 트리 전개
# i번째 단계마다 Promising 검사 (유망한지 안 한지)
# 유망하지 않을 경우 가지치기 / BackTracking

def promising(index, currentWeight):
    global W;
    return (currentWeight + S[index] <= W) and (currentWeight + sum(S[index:]) >= W);

def sum_of_subsets(index, currentWeight, answer):
    global W, num_node;
    num_node += 1;
    if currentWeight == W: #해를 찾은 경우
        print("ANSWER 포함된 INDEX : {}".format(answer)); return; # 해당 가지에서 더 진행할 필요 없음.

    if index == len(S): return; #해를 못 찾은 경우

    if not promising(index, currentWeight): #유망하지 않은 경우
        return; #종료 - 가지치기

    #유망한 경우
    #Weight index번째 포함하는 경우
    answer.append(index);

    sum_of_subsets(index+1, currentWeight + S[index], answer);

    answer.pop();

    #Weight index번째 포함하지 않는 경우
    sum_of_subsets(index+1, currentWeight, answer);


num_node = 0;
S = [1,2,3,4,15];
W = 15;

S.sort(); #오름차순 정렬
sum_of_subsets(0,0,[]);
print("발생한 총 노드 수 (루트 노드 포함) : {}".format(num_node));