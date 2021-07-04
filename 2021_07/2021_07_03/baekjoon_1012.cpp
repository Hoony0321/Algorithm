//1012
#include<iostream>
#include<vector>
using namespace std;

int test_case;
vector<int> result;

void DFS(int y, int x, bool is_first,int M,int N, vector<vector<int>>& map, vector<vector<bool>>& visited){
  if(visited[y][x]) return;
  visited[y][x] = true;

  if(map[y][x] == 0) return;

  if(is_first){
    *(result.end() -1) += 1;
    is_first =false;
  }

  //====== Recursive Start =====//

  //UP
  if(y-1 >= 0){
    DFS(y-1,x,is_first,M,N,map,visited);
  }
  //DOWN
  if(y+1 <= N-1){
    DFS(y+1,x,is_first,M,N,map,visited);
  }
  //LEFT
  if(x-1 >= 0){
    DFS(y,x-1,is_first,M,N,map,visited);
  }
  //RIGHT
  if(x+1 <= M-1){
    DFS(y,x+1,is_first,M,N,map,visited);
  }
}


int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);cout.tie(0);

  cin >> test_case;

  for(int i = 0; i < test_case; i++){
    //하나의 테스트 케이스 시작
    int M,N,cabbage;
    cin >> M >> N >> cabbage;
    vector<vector<int>> map(N,vector<int>(M,0));
    vector<vector<bool>> visited(N,vector<bool>(M,false));

    result.push_back(0);

    for(int j = 0; j < cabbage; j++){
      int y,x;
      cin >> x >> y;
      map[y][x] = 1;
    }

    for(int k = 0; k < N; k++){
      for(int l = 0; l < M; l++){
        DFS(k,l,true,M,N,map,visited);
      }
    }

  }

  for(auto elem : result){
    cout << elem << "\n";
  }


}