//codeup_4021 : 홀수의 합 구하기 - 정올1번문제
#include<iostream>
#include<vector>

using namespace std;

int main(){
  int sum = 0;
  vector<int> numList(7,0);
  for(auto& elem : numList){
    cin >> elem;
  }

  for(auto elem : numList){
    if(elem % 2 != 0){
      sum += elem;
    }
  }

  if(sum == 0) cout << -1 << endl;
  else{
    cout << sum << endl;
  }



}