//2178
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<queue>
using namespace std;
int map[102][102] = {0,};
int N,M;
//방향 = 오른쪽 , 아래 , 왼쪽, 위
int deltaX[4] = {0,1,0,-1}; 
int deltaY[4] = {1,0,-1,0};

struct Pos{
  int x;
  int y;

  Pos(int _x, int _y){x = _x; y = _y;}
};

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

  queue<Pos> bfsQueue; //bfsQueue
  vector<vector<int>> dist(N+2,vector<int>(M+2,0)); //각 노드 최단경로 담는 벡터
  vector<vector<bool>> visited(N+2,vector<bool>(M+2,false));//방문했는지 확인하는 벡터

  bfsQueue.push(Pos(1,1)); //시작노드 1,1 삽입
  dist[1][1] = 1; //시작노드부터 최단거리 1
  visited[1][1] = true;

  while(!bfsQueue.empty()){
    Pos nowPos = bfsQueue.front();
    bfsQueue.pop();

    for(int i = 0; i < 4; i++){
      Pos nextPos = Pos(nowPos.x + deltaX[i], nowPos.y + deltaY[i]);

      //맵 범위 안에 있는지 확인
      if(nextPos.x < 1 && nextPos.x > M && nextPos.y < 1 && nextPos.y > N) continue;
      //길인지 확인
      if(map[nextPos.y][nextPos.x] == 0) continue;
      //방문했던 노드인지 확인
      if(visited[nextPos.y][nextPos.x]) continue;

      bfsQueue.push(nextPos); //queue에 삽입
      dist[nextPos.y][nextPos.x] = dist[nowPos.y][nowPos.x] + 1; //최단거리 입력
      visited[nextPos.y][nextPos.x] = true; //방문 체크
    }
  }

  
  cout << dist[N][M] << "\n";


}