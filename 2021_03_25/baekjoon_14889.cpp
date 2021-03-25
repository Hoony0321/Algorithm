#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>

using namespace std;

int N;
int** S_Map;
int min_diff = 1000000000;

void Calculate(int** S, vector<int>& team1,const
 vector<int>& team2){
  int sum_start = 0;
  for(int i = 0; i < team1.size(); i++){
    for(int j = 0; j < team1.size(); j++){
      sum_start += S[team1[i]][team1[j]];
    }
  }

  int sum_link = 0;
  for(int i = 0; i < team2.size(); i++){
    for(int j = 0; j < team2.size(); j++){
      sum_link += S[team2[i]][team2[j]];
    }
  }

  int diff = abs(sum_start - sum_link);
  if(diff < min_diff) min_diff = diff;
}

void DFS(int index, vector<int> team, const vector<int> remain){
  if(index == N/2){
    Calculate(S_Map,team,remain);
    return;
  }
  
  for(int i = 0; i < remain.size(); i++){
    if(index == 0 || *(team.end()-1) < remain[i]){
      //remain 복사본 생성
      vector<int> temp_remain(remain);
      //temp_remain.resize(remain.size());
      //copy(remain.begin(), remain.end(), temp_remain.begin());

      //DFS실행
      team.push_back(remain[i]);
      temp_remain.erase(temp_remain.begin() + i);
      DFS(index+1,team, temp_remain);

      team.pop_back(); //team배열 원상복구
    }
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N;

  int** S = new int*[N];
  for(int i = 0; i < N; i++){
    S[i] = new int[N];
  }
  S_Map = S;
  for(int i = 0; i < N; i++){
    for(int j = 0; j < N; j++){
      cin >> S[i][j];
    }
  }

  vector<int> team(0);
  vector<int> remain;
  remain.resize(N);
  for(int i = 0; i < N; i++){
    remain[i] = i;
  }

  DFS(0,team,remain);
  

  cout << min_diff << "\n";
  for(int i = 0; i < N; i++){
    delete[] S[i];
  }
  delete[] S;
  S_Map = nullptr;
}