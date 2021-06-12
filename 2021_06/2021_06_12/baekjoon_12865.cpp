#include<iostream>

using namespace std;

int N,K;
int list[104][2];
int max_weight = 0;
int dp[104][100002];

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int N,K;
  cin >> N >> K;

  for(int i = 1; i <= N; i++){
    cin >> list[i][0] >> list[i][1]; //무게,가치 
  }

  for(int i = 1; i <= N; i++){
    for(int j = 1; j <= K; j++){
      if(list[i][0] > j){
        dp[i][j] = dp[i-1][j];
      }
      else{
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-list[i][0]] + list[i][1]);
      }
    }
  }
  
  cout << dp[N][K] << "\n";

}