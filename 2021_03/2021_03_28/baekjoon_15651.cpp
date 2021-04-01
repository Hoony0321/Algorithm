#include<iostream>
#include<vector>
using namespace std;

int N,M;

void BackTracking(int index, vector<int> list ){
  if(index == M){
    for(auto elem : list) cout << elem << " ";
    cout << "\n";
    return;
  }
  

  for(int i = 1; i <= N; i++){
    list.push_back(i);
    BackTracking(index+1, list);
    list.pop_back();
  } 
}

int main(){
  cin >> N >> M;
  vector<int> list;
  BackTracking(0,list);
}