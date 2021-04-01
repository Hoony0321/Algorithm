#include<iostream>
#include<vector>

using namespace std;

int N,M;

void BackTracking(int index, vector<int> selected, int prev){
  if(index == M){
    for(auto elem : selected){cout << elem << " ";}
    cout << "\n";
    return; 
  }

  for(int i = 1; i <= N; i++){
    if(prev <= i){
      selected.push_back(i);
      BackTracking(index+1, selected, i);
      selected.pop_back();
    }
  }  
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N >> M;
  vector<int> list;
  BackTracking(0,list,-1);

}