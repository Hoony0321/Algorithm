//2606
#include<iostream>
#include<vector>
#include<stack>
#include<algorithm>

using namespace std;

int computers,links;
int network[101][101];
stack<int> dfs_stack;
vector<int> is_infected;

void WarmVirus(int start){
  bool visited[computers];
  for(auto& elem : visited){
    elem = false;
  }

  dfs_stack.push(start);

  while(!dfs_stack.empty()){ //stack 비면 종료

    int curNode = dfs_stack.top();
    bool is_connected = false; //연결된 노드가 있는 지 체크하는 bool 변수

    for(int i=1; i <= computers; i++){
      if(visited[i] == false && network[curNode][i] == 1){
        if(find(is_infected.begin(),is_infected.end(),i) == is_infected.end()){ //감염 안 된 index임
          dfs_stack.push(i); //연결된 노드 stack에 넣기
          is_infected.push_back(i); //탐색한 순서 저장하는 배열에 저장
          is_connected=true; //연결된 노드가 있었음을 알려줌.
          break;
        }
      }
    }

    if(!is_connected){
      visited[dfs_stack.top()] = true;
      dfs_stack.pop();
    }

  }

}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);


  cin >> computers >> links;
  for(int i = 0; i < links; i++){
    int link1,link2;
    cin >> link1 >> link2;
    network[link1][link2] = 1;
    network[link2][link1] = 1;
  }

  is_infected.push_back(1);
  WarmVirus(1);

  cout << is_infected.size() -1 << "\n";
}