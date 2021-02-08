#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

//codeup_5136 : No. X=Y=Z - 탐색기반설계

int x,y,z;
int min_operation;

int main(){
  cin >> x >> y >> z;
  vector<int> vec = {x,y,z};
  sort(vec.begin(), vec.end());

  int max_elem  = vec[2];
  int diff = max_elem - vec[0] + max_elem - vec[1];

  if(diff % 2 == 0){
    cout << diff / 2 << endl;
  }
  else{
    cout << (diff+3) / 2 << endl;
  }

}