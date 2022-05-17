# M_Coloring Algorithm
# M가지 색을 인접한 지역이 같은 색이 되지 않도록 색칠하는 문제


def promising(index):
    if(index == -1): # index가 -1일 경우는 검사할 필요 없음.
        return True;

    global n;
    isPromising = True;

    for j in range(0,n):
        if(W[index][j] and vcolor[index] == vcolor[j]): #인접한 지역 중에 같은 색깔이 있을 경우 False return;
            isPromising = False; break;

    return isPromising;

def m_coloring(index):
    global m, num_node;
    num_node += 1;
    if promising(index) :
        if(index == n-1): #종료 조건
            print("answer : {}".format(vcolor));
        else:
            for color in range(1,m+1): #1부터 M까지 색깔 존재
                vcolor[index + 1] = color;
                m_coloring(index+1);
                vcolor[index+1] = 0;


# first Initialize
n = 5; # 노드 수
m = 3; # 색깔 수
num_node = 0; #생성된 노드 수
vcolor = [0 for _ in range(n)]; #색깔 정보를 담고있는 배열

#그래프 연결 정보 담고있는 2차원 배열
W = [[False for _ in range(n)] for _ in range(n)];
W[0][1], W[0][2], W[0][4] = True,True,True;
W[1][0], W[1][2], W[1][3] = True,True,True;
W[2][0], W[2][1], W[2][3] = True,True,True;
W[3][1], W[3][2], W[3][4] = True,True,True;
W[4][0], W[4][3] = True, True;

m_coloring(-1);
print("생성된 노드 수(루트 노드 포함) : {}".format(num_node));