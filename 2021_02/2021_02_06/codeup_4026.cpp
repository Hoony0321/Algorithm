//codeup_4026 : 중앙 값 - 정올1번문제
#include<iostream>
#include<vector>

using namespace std;

void Swap(int& num1, int& num2){
  int temp = num1;
  num1 = num2;
  num2 = temp;
}

void Sorting(vector<int>& vec){
  int min = 0;
  for(int i = 0; i < vec.size()-1; i ++){
    for(int j = i+1; j < vec.size(); j++){
      if(vec[j] < vec[i]) swap(vec[i],vec[j]);
    }
  }
}

int main(){
  vector<int> vec(5,0);
  for(auto& elem : vec){
    cin >> elem;
  }

  Sorting(vec);
  cout << vec[2] << endl;

}