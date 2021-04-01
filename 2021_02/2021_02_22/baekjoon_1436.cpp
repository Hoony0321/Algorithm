#include<iostream>
#include<string>

using namespace std;

int main(){
  int num = 666;
  int order = 1;

  int N;
  cin >> N;

  while(N != order){
    num += 1;
    if(to_string(num).find("666") != string::npos){
      order += 1;
    }
  }

  cout << num << "\n";
}