#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

int N;

int dp[1500001];
int T[1500001];
int M[1500001];

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  
  cin >> N;
  for(int i = 1; i <= N; i++){
    cin >> T[i] >> M[i];
  }


  for(int i = N; i >= 1; i--){
    if(i + T[i] > N+1){ //날짜  초과
      dp[i] = dp[i+1];
    }
    else{ //날짜 초과 X
      dp[i] = max(dp[i+1], M[i] + dp[i+T[i]]);
    }
  }

  cout << dp[1] << "\n";

}
	

