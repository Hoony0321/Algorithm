#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL); 


  int N;
  cin >> N;
  vector<int> timeList(N,0);
  for(int i = 0; i < N; i++){
    cin >> timeList[i];
  }

  sort(timeList.begin(), timeList.end());

  int prev = 0;
  int sum =0;
  for(int i = 0; i < N; i++){
    timeList[i] = prev + timeList[i];
    prev = timeList[i];
    sum += timeList[i];
  }

  cout << sum << "\n";

}