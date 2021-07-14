//1697
#include<iostream>
#include<deque>
#include<vector>
using namespace std;

#define MAX 100000

int N,K;

struct pos{
  int x;
  int turn;
  pos(int _x, int _turn){x = _x; turn = _turn;}
};

int main(){
  cin >> N >> K;


  deque<pos> bfsQueue;
  vector<bool> visited(MAX,false);
  bfsQueue.push_back(pos(N,0));

  int min = -1;
  while(!bfsQueue.empty()){
    pos curPos = bfsQueue.front();
    int nextPosList[3] = {curPos.x-1, curPos.x+1, curPos.x*2};
    bfsQueue.pop_front();

    for(int i = 0; i < 3; i++){
      pos nextPos = pos(nextPosList[i],curPos.turn+1);

      //영역 안에 있는지 확인
      if(nextPos.x < 0 || nextPos.x > MAX) continue;
      //방문했던 곳인지 확인
      if(visited[nextPos.x]) continue;

      
      if(nextPos.x == K) {min = nextPos.turn; break;}
      bfsQueue.push_back(nextPos);
      visited[nextPos.x] = true;
    }

    if(min != -1) break;
  }

  cout << min << "\n";

}