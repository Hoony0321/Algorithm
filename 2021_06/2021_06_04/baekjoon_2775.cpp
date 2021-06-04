#include<iostream>

using namespace std;

int array[15][15] = {0};

int FindNum(int k, int n){
  if(n == 1) array[k][n] = 1;
  else if(array[k][n] == 0){
    array[k][n] = FindNum(k,n-1) + FindNum(k-1,n);
  }
  return array[k][n];
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  for(int i = 0; i < 15; i++){
    array[0][i] = i;
  }
  int testCase;
  cin >> testCase;
  for(int i = 0; i < testCase; i++){
    int k,n;
    cin >> k >> n;
    cout << FindNum(k,n) << "\n";
  }
}