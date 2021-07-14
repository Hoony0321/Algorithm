//2206
#include<iostream>
#include<vector>
#include<string>
#include<deque>

using namespace std;

#define MAX 1001

int N,M;
int map[MAX][MAX];
bool visited[2][MAX][MAX]; //부수기 전 / 후 방문 기록  => 0이 전, 1이 후
//아래 오른쪽 왼쪽 위
int deltaY[4] = {1,0,0,-1};
int deltaX[4] = {0,1,-1,0};

struct vertex{
  int y; int x; int cnt; bool crush;
  
  vertex(int _y, int _x, int _cnt, bool _crush){
    y = _y; x = _x; cnt = _cnt; crush = _crush;
  }
};

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);

  cin >> N >> M;
  for(int i = 0; i < N; i++){
    string inputVal;
    cin >> inputVal;
    for(int j = 0; j < M; j++){
      map[i+1][j+1] = inputVal[j] - '0';
    }
  }

  deque<vertex> bfsQueue;
  //첫번째 (1,1)에서 시작
  vertex startPoint = vertex(1,1,1,false);
  visited[0][startPoint.y][startPoint.x] = true;
  bfsQueue.push_back(startPoint);

  int answer = -1;
  bool firstCrush = false;
  while(!bfsQueue.empty()){
    vertex nowPoint = bfsQueue.front();
    bfsQueue.pop_front();

    if(nowPoint.y == N && nowPoint.x == M){
      if(answer == -1) answer = nowPoint.cnt;
      else if(answer > nowPoint.cnt) answer = nowPoint.cnt;
    }

    for(int i = 0; i < 4; i++){
      vertex nextPoint = vertex(nowPoint.y + deltaY[i] , nowPoint.x + deltaX[i], nowPoint.cnt + 1, nowPoint.crush);

      //방문했던 곳인지 확인
      if((!nextPoint.crush && visited[0][nextPoint.y][nextPoint.x]) || (nextPoint.crush &&
        visited[1][nextPoint.y][nextPoint.x])) continue;
      //범위 안에 있는 곳인지 확인
      if(nextPoint.y < 1 || nextPoint.y > N || nextPoint.x < 1 || nextPoint.x > M) continue;
      
      //nextPoint 위치가 벽일 경우
      if(map[nextPoint.y][nextPoint.x] == 1){
        if(nextPoint.crush) continue; //이미 벽을 뚫은 적이 있으므로 continue
        else nextPoint.crush = true;
      }

      if(nextPoint.crush) visited[1][nextPoint.y][nextPoint.x] = true;
      else{ visited[0][nextPoint.y][nextPoint.x] = true;}
      bfsQueue.push_back(nextPoint);

    }
  }

  cout << answer << "\n";
}
  
  

