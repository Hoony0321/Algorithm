//baekjoon 22113 - 2021 연세대학교 미래캠퍼스 제2회 슬기로운 코딩생활 Open Contest
#include<iostream>
#include<deque>
#include<vector>

using namespace std;

int main(){
  int N,M;
  cin >> N >> M;
  
  deque<int> usedBus;
  for(int i = 0; i < M; i++){
    int num;
    cin >> num;
    usedBus.push_back(num-1);
  }

  vector<vector<int>> busFare(N,vector<int>(N,0));
  for(int i = 0; i < N; i++){
    for(int j = 0; j < N; j++){
      cin >> busFare[i][j];
    }
  }

  int needFare = 0;
  int curBus = usedBus.front();
  usedBus.pop_front();
  while(!usedBus.empty()){
    int nextBus = usedBus.front();
    usedBus.pop_front();

    needFare += busFare[curBus][nextBus];
    curBus = nextBus;
  }

  cout << needFare << "\n";
}