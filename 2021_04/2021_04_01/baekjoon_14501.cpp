#include<iostream>
#include<vector>

using namespace std;

int N;
vector<pair<int,int>> schedule;
int max_pay = 0;
void DFS(int day, int pay){
  if(pay > max_pay && day <= N) max_pay = pay;

  if(day >= N){ //종료 조건
    return;
  }

  for(int i = day; i < N; i++){
    DFS(day + schedule[i].first, pay + schedule[i].second);
    day += 1;
  }

}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);
 cin >> N;
 for(int i = 0; i < N; i++){
   int T,P;
   cin >> T >> P;
   schedule.push_back(make_pair(T,P));
 }

 DFS(0,0);
 cout << max_pay << "\n";
}