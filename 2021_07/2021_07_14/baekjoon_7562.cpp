#include<iostream>
#include<deque>
#include<vector>

struct pos{
  int y; int x; int cnt;
  pos(int _y, int _x, int _cnt){
    y = _y; x = _x; cnt = _cnt;
  }
};

using namespace std;

int deltaY[8] = {-1,-2,-2,-1,1,2,2,1};
int deltaX[8] = {-2,-1,1,2,2,1,-1,-2};



int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);

  int testCase;
  cin >> testCase;

  for(int i = 0; i < testCase; i++){
    int size;
    pos startPoint(0,0,0);
    pos destPoint(0,0,0);
    
    cin >> size;
    cin >> startPoint.y >> startPoint.x;
    cin >> destPoint.y >> destPoint.x;

    vector<vector<bool>> visited(size,vector<bool>(size,false));
    deque<pos> bfsQueue;
    int answer = -1;

    //처음 시작 위치 넣기.
    visited[startPoint.y][startPoint.x] = true;
    bfsQueue.push_back(startPoint);

    while(!bfsQueue.empty()){
      pos nowPos = bfsQueue.front();
      bfsQueue.pop_front();

      //목적지인지 확인
      if(nowPos.y == destPoint.y && nowPos.x == destPoint.x){answer = nowPos.cnt; break;}

      for(int p = 0; p < 8; p++){
        pos nextPos = pos(nowPos.y + deltaY[p], nowPos.x + deltaX[p], nowPos.cnt + 1);

        //영역 안에 있는지 확인
        if(nextPos.y < 0 || nextPos.y >= size || nextPos.x < 0 || nextPos.x >= size) continue;
        //방문한 지역인지 확인
        if(visited[nextPos.y][nextPos.x]) continue;

        visited[nextPos.y][nextPos.x] = true;
        bfsQueue.push_back(nextPos);
      }

    }

    cout << answer << "\n";






  }
}