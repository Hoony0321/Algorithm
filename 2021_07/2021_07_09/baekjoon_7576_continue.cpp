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
  int x; int y;
  pos(int _y, int _x){
    x = _x; y = _y;
  }
}

int main(){
  cin >> N >> M;

  vector<pos> spray;
  for(int i = 1; i <= N; i++){
    for(int j = 1; j <= M; j++){
      cin >> box[i][j];
      if(box[i][j] == 1)spray.push_back(box[i][j]);
    }
  }

  for(int i = 0; i < spray.size(); i++){
    queue<pos> bfsQueue;
    vector<vector<int>> day(N+2, vector<int>(M+2,-1));
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
      }
      
    }
  }


  //처음 위치 넣기.

  while(!bfsQueue.empty()){

  }
  

}