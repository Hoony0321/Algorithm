#include<iostream>

using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);

  int N;
  int num_dot = 1;
  int checkNum = 1;
  cin >> N;

  while(true){
    if(N % 2 == 0 || N % 5 == 0){ num_dot = -1; break;}
    if(checkNum % N == 0){
      break;
    }
    else{
      checkNum = (checkNum * 10 + 1) % N;
      num_dot += 1;
    }
  }

  cout << num_dot << "\n";
}