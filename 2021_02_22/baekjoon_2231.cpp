#include<iostream>
#include<string>
using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL);
  int N;
  cin >> N;

  int digit = to_string(N).size();
  bool found = false;
  int generator = N - digit * 9;

  while(generator < N && !found){
    
    int sum = generator;
    int temp = generator;
    while(temp > 0){
      sum += temp % 10;
      temp /= 10;
    }
    if(sum == N) found = true;
    generator += 1;
  }

  if(found) cout << generator - 1 << "\n";
  else cout << 0 << "\n";

}