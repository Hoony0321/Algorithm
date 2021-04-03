#include<iostream>

using namespace std;

int R,C;
char map[252][252] = {'x',};
bool visited[252][252] = {false,};
int survive[2] = {0,0};

void DFS(int y, int x, int& sheep, int& wolf){
  if(visited[y][x] == true){ //이미 방문
    return;
  }

  //방문 시작
  visited[y][x] = true;

  if(map[y][x] == '#'){return;} //울타리
  else if(map[y][x] == 'o'){sheep += 1;}
  else if(map[y][x] == 'v'){wolf += 1;}

  //왼쪽
  if(x-1 >= 1){DFS(y,x-1,sheep,wolf);}
  //오른쪽
  if(x+1 <= C){DFS(y,x+1,sheep,wolf);}
  //위쪽
  if(y-1 >= 1){DFS(y-1,x,sheep,wolf);}
  //아래쪽
  if(y+1 <= R){DFS(y+1,x,sheep,wolf);}


}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> R >> C;
  for(int i = 1; i <= R; i++){
    for(int j = 1; j <= C; j++){
      cin >> map[i][j];
    }
  }

  for(int i = 1; i <= R; i++){
    for(int j = 1; j <= C; j++){
      int sheep = 0;
      int wolf = 0;
      DFS(i,j,sheep,wolf);
      if(sheep > wolf) wolf = 0;
      else sheep = 0;
      survive[0] += sheep;
      survive[1] += wolf;
    }
  }

  cout << survive[0] << " " << survive[1] << "\n";
}