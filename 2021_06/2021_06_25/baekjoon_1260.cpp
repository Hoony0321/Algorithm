//1260
#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<deque>
using namespace std;

int N; // 정점 개수
int M; // 간선 개수
int V; //탐색 시작할 정점 번호
int graph[1001][1001];
queue<int> queue_bfs;
deque<int> stack_dfs;
vector<int> dfsList;
vector<int> bfsList;

void DFS(){
  if(stack_dfs.size() == 0){ return; } //탐색 끝

  int top = stack_dfs.front();
  stack_dfs.pop_front();
  if(find(dfsList.begin() , dfsList.end(), top) != dfsList.end()){DFS(); return;}
  dfsList.push_back(top);
  
  for(int i = N; i >= 1; i--){
    if(graph[top][i] == 1){ //간선 존재
      if(find(dfsList.begin(), dfsList.end(), i) == dfsList.end()){stack_dfs.push_front(i); }
    }
  }

  DFS();
}

void BFS(int from){
  for(int i = 1; i <= N; i++){
    if(graph[from][i] == 1){ //간선 존재
      if(find(bfsList.begin(), bfsList.end(), i) == bfsList.end()){//방문했던 정점 아님
        bfsList.push_back(i);
        queue_bfs.push(i);
      }
    }
  }

  if(queue_bfs.size() != 0){
    int element = queue_bfs.front();
    queue_bfs.pop();
    BFS(element);
  }


}

int main(){
 cin >> N >> M >> V;
 for(int i = 0; i < M; i++){
   int vertex1,vertex2;
   cin >> vertex1 >> vertex2;
   graph[vertex1][vertex2] = 1;
   graph[vertex2][vertex1] = 1;
 }

 stack_dfs.push_front(V);
 DFS();
 for(auto elem : dfsList){
   cout << elem << " ";
 }
 cout << "\n";

 bfsList.push_back(V);
 BFS(V);
 for(auto elem: bfsList){
   cout << elem << " ";
 }
 cout << "\n";
 
}