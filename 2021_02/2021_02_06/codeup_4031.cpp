//codeup_4031 : 가장 큰 수 - 정올 1번 문제
#include<iostream>
#include<vector>

using namespace std;



int main(){
  int max_even = 0;
  int max_odd = 0;

  int num;
  for(int i = 0; i < 7; i++){
    cin >> num;
    if(num % 2 == 0){
      if(max_even < num) max_even =num;
    }
    else{
      if(max_odd < num) max_odd=num;
    }
  }

  cout << max_even + max_odd << endl;

}

