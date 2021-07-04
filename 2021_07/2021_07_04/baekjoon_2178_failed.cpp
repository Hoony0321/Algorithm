//2178
#include<iostream>
#include<string>
#include<vector>
using namespace std;
int map[101][101] = {0,};
int N,M;
int result = 10000;

void DFS(int y, int x,int past,vector<vector<bool>> visited){
  if(visited[y][x]) return;
  visited[y][x] = true;

  if(map[y][x] == 0) return;
  past += 1;
  
  if(y == N && x == M){
    if(result > past)result = past;
    visited[y][x] = false;
    return;
  }

  //UP
  if(y-1 >= 1){DFS(y-1,x,past,visited);}
  //DOWN
  if(y+1 <= N){DFS(y+1,x,past,visited);}
  //LEFT
  if(x-1 >= 1){DFS(y,x-1,past,visited);}
  //RIGHT
  if(x+1 <= M){DFS(y,x+1,past,visited);}
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);
  cin >> N >> M;

  for(int i = 1; i <= N; i++){
    string input;
    cin >> input;
    for(int j = 1; j <= M; j++){
      map[i][j] = input[j-1] - '0';
    }
  }

  vector<vector<bool>> visited(N+1,vector<bool>(M+1,false));

  DFS(1,1,0,visited);

  cout << result << "\n";

}