#include<iostream>

using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL);

  int N,K;
  cin >> N >> K;
  
  int coinList[10];
  for(int i = 0 ; i < N; i++){
    cin >> coinList[i];
  }

  int coin_required = 0;
  while(K>0){
    for(int i = N-1; i >= 0; i--){
      if(K >= coinList[i]){
        int coin = K / coinList[i];
        coin_required += coin;
        K -= coin * coinList[i];
      }
    }
  }

  cout << coin_required << "\n";
}