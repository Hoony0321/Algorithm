//7569
#include<iostream>
#include<vector>
#include<deque>

#define MAX 102

using namespace std;

struct pos{
  int z; int y; int x;
  pos(int _z, int _y, int _x){z = _z; y = _y; x = _x;}
};

int H,N,M;
int box[MAX][MAX][MAX];
bool visited[MAX][MAX][MAX];
deque<pos> bfsQueue;

//위, 아래 , 앞 , 뒤 , 왼쪽, 오른쪽
int deltaX[6] = {0,0,0,0,-1,1};
int deltaY[6] = {0,0,1,-1,0,0};
int deltaZ[6] = {-1,1,0,0,0,0};

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);cout.tie(0);

  cin >> M >> N >> H;

  vector<vector<vector<int>>> day(H+2, vector<vector<int>>(N+2,vector<int>(M+2,-1)));
  for(int i = 1; i <= H; i++){
    for(int j = 1; j <= N; j++){
      for(int k = 1; k <= M; k++){
        int tomato;
        cin >> tomato;
        box[i][j][k] = tomato;
        if(tomato == 1){
          visited[i][j][k] = true;
          day[i][j][k] = 0;
          bfsQueue.push_back(pos(i,j,k));
        }
      }
    }
  }

  while(!bfsQueue.empty()){
    pos nowPos = bfsQueue.front();
    bfsQueue.pop_front();

    for(int i = 0; i < 6; i++){
      pos nextPos = pos(nowPos.z + deltaZ[i], nowPos.y + deltaY[i], nowPos.x + deltaX[i]);

      //방문했던 곳인지 확인
      if(visited[nextPos.z][nextPos.y][nextPos.x]) continue;
      //범위 안에 포함되는 지 확인
      if(nextPos.z < 1 || nextPos.z > H || nextPos.y < 1 || nextPos.y > N || nextPos.x < 1 || nextPos.x > M) continue;
      //토마토인지 확인
      if(box[nextPos.z][nextPos.y][nextPos.x] != 0) continue;
      //이미 더 짧은 시간이 있는지 확인
      if(day[nextPos.z][nextPos.y][nextPos.x] != -1 &&
        day[nextPos.z][nextPos.y][nextPos.x] < day[nowPos.z][nowPos.y][nowPos.x] + 1) continue;

      visited[nextPos.z][nextPos.y][nextPos.x] = true;
      day[nextPos.z][nextPos.y][nextPos.x] = day[nowPos.z][nowPos.y][nowPos.x] + 1;
      bfsQueue.push_back(nextPos);
    }

  }
  
  bool isAvailable = true;
  int max = -1;
  for(int i = 1; i <= H; i++){
    for(int j = 1; j <= N; j++){
      for(int k = 1; k <= M; k++){
        if(day[i][j][k] == -1 && box[i][j][k] == 0) isAvailable = false;
        else{
          if(day[i][j][k] > max) max = day[i][j][k];
        }
      }
    }
  }

  if(isAvailable) cout << max << "\n";
  else {cout << -1 << "\n";}
}