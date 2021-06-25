#include<iostream>
#include<vector>
using namespace std;

int N,B,C;
vector<int> testRoom;

int SuperVisorNum(int people){
  int supervisor = 1;
  people -= B;
  if(people > 0){
    supervisor += people / C;
    if(people % C != 0) supervisor += 1;
  }

  return supervisor;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);cout.tie(0);
  cin >> N;
  for(int i = 0; i < N; i++){
    int people;
    cin >> people;
    testRoom.push_back(people);
  }

  cin >> B >> C;

  long long int sum = 0;
  for(int i =0; i < N; i++){
    sum += SuperVisorNum(testRoom[i]);
  }

  cout << sum << "\n";
}