#include<iostream>
#include<vector>

using namespace std;

void BackTracking(int N, int M, vector<int> selected,vector<bool> numlist, int prev){
  if(selected.size() == M){
    for(auto elem : selected){
      cout << elem << " ";
    }
    cout << "\n";
    return;
  }

  for(int i = 0; i < N; i++){
    if(numlist[i] == false && prev < i){
      selected.push_back(i+1);
      numlist[i] = true;
      BackTracking(N,M,selected,numlist,i);
      selected.pop_back();
      numlist[i] = false;
    }
  }
}

int main(){
  int N,M;
  cin >> N >> M;
  vector<int> selected;
  vector<bool> numlist(N,false);
  BackTracking(N,M,selected,numlist,-1);
}