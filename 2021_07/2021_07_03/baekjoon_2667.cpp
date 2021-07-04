//2667
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;

int N;
int map[26][26];
bool visited[26][26] = {false,};
vector<int> result;

void DFS(int y, int x, bool is_first){
  if(visited[y][x]) return;
  visited[y][x] = true;

  if(map[y][x] == 0) return;

  if(is_first){
    result.push_back(1);
    is_first = false;
  }
  else{
    *(result.end()-1) += 1;  
  }

  //======Recursiving Start=======//

  //UP
  if(y-1 >= 1){
    DFS(y-1,x,is_first);
  }
  //DOWN
  if(y+1 <= N){
    DFS(y+1,x,is_first);
  }
  //LEFT
  if(x-1 >= 0){
    DFS(y,x-1,is_first);
  }
  //RIGHT
  if(x+1 <= N){
    DFS(y,x+1,is_first);
  }

}

int main(){
  cin >> N;
  for(int i = 1; i <= N; i++){
    string input;
    cin >> input;
    for(int j = 0; j < input.size(); j++){
      map[i][j+1] = input[j] - '0';
    }
  }

  for(int i = 1; i <= N; i++){
    for(int j = 1; j <= N; j++){
      DFS(i,j,true);
    }
  }


  cout << result.size() << "\n";
  sort(result.begin(),result.end());
  for(auto elem : result){
    cout << elem << "\n";
  }
}