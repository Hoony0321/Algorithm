//baekjoon 22114 - 2021 연세대학교 미래캠퍼스 제2회 슬기로운 코딩생활 Open Contest
#include<iostream>
#include<deque>
#include<vector>

#define MAX 100
using namespace std;

int dp[2][MAX];


int N,K;
int length[MAX];
int result = 1;
void dfs(int pos, bool jump, int step){
  if(pos == N) return;
  if(jump){ //이미 점프한 경우
    if(length[pos] <= K && dp[1][pos+1] < step + 1){
      dp[1][pos+1] = step + 1;
      dfs(pos+1,jump,step+1);
    }
  }
  else{ //점프를 안 한 경우
    if(length[pos] <= K){
      if(dp[0][pos+1] < step + 1){
         dp[0][pos+1] = step + 1;
         dfs(pos+1,jump,step+1);
       }
    } 
    else{
      jump = true;
      if(dp[1][pos+1] < step + 1){
        dp[1][pos+1] = step  + 1;
        dfs(pos+1, jump, step+1);
      }
    }
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);
  cin >> N >> K;
  for(int i = 1; i < N; i++){
    cin >> length[i];
  }

  for(int i = 1; i <= N; i++){
    dp[0][i] = 1;
    dp[1][i] = 1;
  }

  for(int i = 1; i < N; i++){
    dfs(i,false,1);
  }
  
  for(int i = 1; i <= N; i++){
    result = result < dp[0][i] ? dp[0][i] : result;
    result = result < dp[1][i] ? dp[1][i] : result;
  }

  cout << result << "\n";
}