#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int K;
char course[50];
vector<pair<int,int>> PosList;
int min_x = 50;
int min_y = 50;
int max_x = -50;
int max_y = -50;
//북 동 남 서
int direction[4][2] = {{-1,0},{0,+1},{+1,0},{0,-1}};

void CheckPosition(int y, int x){
  if(y < min_y) min_y = y;
  else if(y > max_y) max_y = y;
  if(x < min_x) min_x = x;
  else if(x > max_x) max_x = x;

  vector<pair<int,int>>:: iterator iter;
  iter = find(PosList.begin(),PosList.end(),make_pair(y,x));
  if(iter == PosList.end()){
    PosList.push_back(make_pair(y,x));
  }
}



int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);


  cin >> K;
  for(int i = 0; i < K; i++){
    cin >> course[i];
  }

  int y = 0;
  int x = 0;
  int dir = 2; // 남
  for(int i = 0; i < K; i++){
    CheckPosition(y, x);
    switch(course[i]){
      case 'F':
        y += direction[dir][0];
        x += direction[dir][1];
        break;
      case 'R':
        dir = (dir + 1)%4;
        break;
      case 'L':
        dir = (dir - 1)%4;
        break;
    }
  }
  CheckPosition(y, x);

  int required_x = max_x - min_x + 1;
  int required_y = max_y - min_y + 1;
  vector<vector<char>> map(required_y,vector<char>(required_x,'#'));
  //int offsetX = abs(min_x);
  //int offsetY = abs(min_y);

  for(auto elem : PosList){
    /*
    cout << "PosList : ";
    cout << elem.first << " " << elem.second << "\n";*/
    map[elem.first + abs(min_y)][elem.second + abs(min_x)] = '.';
  }

  
  for(int i = 0; i <required_y; i++){
    for(int j = 0; j < required_x; j++){
      cout << map[i][j] << " ";
    }
    cout << "\n";
  }
  



}