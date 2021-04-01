#include<iostream>
#include<vector>
#include<cmath>

using namespace std;

int N; // 1 <= N <= 15
int answer = 0;

void BackTracking(int step, vector<int> selected, vector<bool> numList){
  if(step == N){
    answer += 1;
    return;
  }
  for(int i = 0; i < N; i++){
    bool check = true;
    if(numList[i] == true){
      selected.push_back(i);
      numList[i] = false;
      for(int k = 0; k < step; k++){
        if(abs(k - step) == abs(selected[k] - selected[step])){
          check = false;
        }
      }
      if(check == true) BackTracking(step+1,selected,numList);
      selected.pop_back();
      numList[i] = true;      
    }
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> N;
  vector<int> map;
  vector<bool> numList(N,true);
  for(int i = 0; i < N; i++){
    map.push_back(i);
    numList[i] = false;
    BackTracking(1,map,numList);
    map.pop_back();
    numList[i] = true;
  }
  

  cout << answer << "\n";
}