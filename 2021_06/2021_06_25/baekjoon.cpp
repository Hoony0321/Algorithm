//1260
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int N; // 정점 개수
int M; // 간선 개수
int V; //탐색 시작할 정점 번호
int graph[1001][1001];
vector<int> dfsList;
vector<int> bfsList;

void DFS(int from){
  int min = N+1;
  bool stop = true;
  for(int i = 1; i <= N; i++){
    if(graph[from][i] == 1){ //간선 존재
      if(find(dfsList.begin(), dfsList.end(),i) == dfsList.end()){//이전에 방문했던 정점 아님
        if(min > i) {stop = false; min = i;}
      }
    }
  }
  if(!stop){ dfsList.push_back(min);  DFS(min);}
}

int main(){
 cin >> N >> M >> V;
 for(int i = 0; i < M; i++){
   int vertex1,vertex2;
   cin >> vertex1 >> vertex2;
   graph[vertex1][vertex2] = 1;
   graph[vertex2][vertex1] = 1;
 }

 dfsList.push_back(V);
 DFS(V);
 for(auto elem : dfsList){
   cout << elem << " ";
 }
 
}