//baekjoon_1008 - A/B

#include<iostream>

using namespace std;

int main(){
  int a, b;
  cin >> a >> b;
  double result = (double)a/(double)b;

  cout << fixed;
  cout.precision(12);
  cout << result << endl;

}