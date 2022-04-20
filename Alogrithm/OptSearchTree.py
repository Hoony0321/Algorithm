#최적이진검색트리

def printMatrix(m):
    for i in range(1,len(m) -1):
        for j in range(1,len(m) -1):
            print(m[i][j], end= ' ')
        print()

class Node:
    def __init__(self,data):
        self.left_child = None
        self.right_child = None
        self.data = data

def tree(i,j,R,keys):
    k = R[i][j]
    if k == 0:
        return
    else:
        node = Node(keys[k])
        node.left_child = tree(i,k-1,R,keys)
        node.right_child = tree(k+1,j,R,keys)
        return node

def in_order(root,result):
    if root != None:
        in_order(root.left_child,result)
        result.append(root.data)
        in_order(root.right_child,result)

def pre_order(root,result):
    if root != None:
        result.append(root.data)
        pre_order(root.left_child,result)
        pre_order(root.right_child,result)

def post_order(root,result):
    if root != None:
        post_order(root.left_child,result)
        post_order(root.right_child,result)
        result.append(root.data)



def optSearchTree(n, P, A,R):

    for i in range(1,n+1):
        A[i][i-1] = 0
        A[i][i] = P[i]
        R[i][i] = i
        R[i][i-1] = 0

    A[n+1][n] = 0
    R[n+1][n] = 0

    for diagonal in range(1,n): #1부터 n-1까지 탐색
        for i in range(1,n - diagonal +1):
            j = i + diagonal
            for k in range(i,j+1): #i부터 j까지
                originVal = A[i][j]
                A[i][j] = min(A[i][j], A[i][k-1] + A[k+1][j] + sum(P[i:j+1]))
                if originVal != A[i][j]: #값 변경이 일어남 - 해당 K 값 저장
                    R[i][j] = k

    return A[1][n]

#test case
# n = 4
# dataSet = [None,'A','B','C','D']
# P = [None] + [3/8, 3/8, 1/8, 1/8]
# A = [[float('INF') for _ in range(n+2)] for _ in range(n+2)] #최소 탐색 시간 담을 배열
# R = [[0 for _ in range(n+2)] for _ in range(n+2)] #최적 탐색 경로 담을 배열
# print(optSearchTree(n,P,A,R))
# printMatrix(A)
# printMatrix(R)
#
# rootNode = tree(1,n,R,dataSet)
# tree_arr = []
# in_order(rootNode,tree_arr)
# print(tree_arr)
#
# tree_arr = []
# pre_order(rootNode,tree_arr)
# print(tree_arr)

#case 1
n = 5
dataSet = [None,'A','B','C','D','E']
P = [None] + [i/15 for i in range(5)]
A = [[float('INF') for _ in range(n+2)] for _ in range(n+2)] #최소 탐색 시간 담을 배열
R = [[0 for _ in range(n+2)] for _ in range(n+2)] #최적 탐색 경로 담을 배열
print(optSearchTree(n,P,A,R))
printMatrix(R)

rootNode = tree(1,n,R,dataSet)
tree_arr = []
in_order(rootNode, tree_arr)
print(tree_arr)

tree_arr = []
pre_order(rootNode, tree_arr)
print(tree_arr)

tree_arr = []
post_order(rootNode, tree_arr)
print(tree_arr)

#case 2
n = 8
dataSet = [None,'A','B','C','D','E','F','G','H']
P = [None] + [1/8 for _ in range(8)]
A = [[float('INF') for _ in range(n+2)] for _ in range(n+2)] #최소 탐색 시간 담을 배열
R = [[0 for _ in range(n+2)] for _ in range(n+2)] #최적 탐색 경로 담을 배열
print(optSearchTree(n,P,A,R))
printMatrix(R)

rootNode = tree(1,n,R,dataSet)
tree_arr = []
in_order(rootNode, tree_arr)
print(tree_arr)

tree_arr = []
pre_order(rootNode, tree_arr)
print(tree_arr)

tree_arr = []
post_order(rootNode, tree_arr)
print(tree_arr)