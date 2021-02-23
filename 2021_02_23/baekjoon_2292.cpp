#include<iostream>

using namespace std;

int main(){
  int N;
  cin >> N;
  N -= 1;
  int rayer = 0;
  while(N > 0){
    rayer += 1;
    N -= rayer * 6;
    
  }
  cout << rayer+1 << "\n";

}