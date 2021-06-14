#include<iostream>

using namespace std;

int N;
int DP[1000001] ={0,1,2};

int RecursiveFunc(int n){
  ios_base::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);
  if(DP[n] != 0) return DP[n];

  DP[n] = (RecursiveFunc(n-1) + RecursiveFunc(n-2)) % 15746;
  return DP[n];
}

int main(){
  cin >> N;
  cout << RecursiveFunc(N)<< "\n";
}