#include<iostream>
#include<algorithm>

using namespace std;

int T;
int dp[41][2] = {{1,0},{0,1}};

pair<int,int> FindResult(int index){
  if(dp[index][0] != 0 || dp[index][1] != 0){
    return make_pair(dp[index][0] , dp[index][1]);
  }

  pair<int,int> value1 = FindResult(index-1);
  pair<int,int> value2 = FindResult(index-2);
  dp[index][0] = value1.first + value2.first;
  dp[index][1] = value1.second + value2.second;

  return make_pair(dp[index][0] , dp[index][1]);
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  cin >> T;
  for(int i = 0; i < T; i++){
    int input;
    cin >> input;
    pair<int,int> result = FindResult(input);
    cout << result.first << " " << result.second << "\n";
  }




}