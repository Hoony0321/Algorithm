#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

//codeup_5136 : No. X=Y=Z - 탐색기반설계
//DFS로 풀 수 있을듯

int x,y,z;
int min_operation = 30;

bool CheckAvailablity(int index){ // pruning cases
  if(index == min_operation) return false;
  return true;
}

bool CheckEqual(vector<int> vec){
  if(vec[0] == vec[1] && vec[1] == vec[2]) return true;
  return false;
}

void DFS(int, vector<int>);

void FindingMinimumOperation(int index, vector<int> vec){
  if(CheckAvailablity(index) == false) return; //pruning cases;
  if(CheckEqual(vec) == true){
    if(min_operation > index) {
      min_operation = index;
    }
    return;
  }

  DFS(index, vec);

}




int main(){
  cin >> x >> y >> z;
  vector<int> vec = {x,y,z};

  FindingMinimumOperation(0,vec);

  cout << min_operation << endl;
}

void DFS(int index, vector<int> vec){
  sort(vec.begin(),vec.end());
  FindingMinimumOperation(index+1, {vec[0] + 1,vec[1] + 1,vec[2]});
  FindingMinimumOperation(index+1, {vec[0]+2,vec[1],vec[2]});

}