//7576
#include<iostream>
#include<queue>
#include<vector>

using namespace std;

int box[1002][1002];
int N,M;
//상, 하 , 좌, 우
int deltaY[4] = {-1,1,0,0};
int deltaX[4] = {0,0,-1,1};

struct pos{
  int x;
  int y;
  pos(int _y, int _x){
    y = _y;  x = _x;
  }
};

int main(){
  cin >> M >> N;

  vector<pos> spray;
  for(int i = 1; i <= N; i++){
    for(int j = 1; j <= M; j++){
      cin >> box[i][j];
      if(box[i][j] == 1) spray.push_back(pos(i,j));
    }
  }


  vector<vector<int>> day(N+2, vector<int>(M+2,-1));

  for(int i = 0; i < spray.size(); i++){
    queue<pos> bfsQueue;
    vector<vector<bool>> visited(N+2,vector<bool>(M+2,false));

    //처음 퍼뜨리는 위치 넣기
    pos firstPos = spray[i];
    bfsQueue.push(firstPos);
    day[firstPos.y][firstPos.x] = 0;
    visited[firstPos.y][firstPos.x] = true;

    while(!bfsQueue.empty()){
      pos nowPos = bfsQueue.front();
      bfsQueue.pop();

      for(int i = 0; i < 4; i++){
        pos nextPos = pos(nowPos.y + deltaY[i], nowPos.x + deltaX[i]); //탐색할 위치 잡기.

        //범위 확인
        if(nextPos.x < 1 || nextPos.x > M || nextPos.y < 1 || nextPos.y > N) continue;
        //방문했던 영역인지 확인
        if(visited[nextPos.y][nextPos.x]) continue;
        //안 익은 토마토인지 확인
        if(box[nextPos.y][nextPos.x] != 0) continue;
        //이미 더 짧은 day가 있는지 확인
        if(day[nextPos.y][nextPos.x] != -1 && day[nextPos.y][nextPos.x] < day[nowPos.y][nowPos.x] + 1) continue;

        day[nextPos.y][nextPos.x] = day[nowPos.y][nowPos.x] + 1;
        visited[nextPos.y][nextPos.x] = true;
        bfsQueue.push(nextPos);
      }
      
    }
  }

  for(int i = 1; i <= N; i++){
    for(int j = 1; j <= M; j++){
      cout << day[i][j] << " ";
    }
    cout << "\n";
  }

}