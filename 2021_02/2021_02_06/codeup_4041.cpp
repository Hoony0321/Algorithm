//codeup_4041 : 숫자 다루기 - 정올1번문제
#include<iostream>
#include<vector>
using namespace std;

vector<int> numlist;

int main(){
  int num;
  int temp;
  int sum = 0;
  cin >> num;
  while(num > 0){
    temp = num % 10;
    numlist.push_back(temp);
    num -= temp;
    num /= 10;
  }

  bool first = true;
  for(int i = 0; i < numlist.size(); i++){
    if(numlist[i] == 0){
      if(first == false){
        cout << numlist[i];
      }
    }
    else{
      first = false;
      sum += numlist[i];
      cout << numlist[i];
    }
  }
  cout << endl;
  cout << sum <<endl;
}
