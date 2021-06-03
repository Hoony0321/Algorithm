#include<iostream>

using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int X;
  cin >> X;

  int index = 1;
  int sum = 0;

  while(true){
    sum += index;
    if(sum >= X){break;}
    index++;
  }

  int distance = X - (sum - index);
  if(index % 2 == 0){
    cout << to_string(distance) + "/" + to_string(index - distance +1) << "\n";
  }
  else{
    cout << to_string(index - distance + 1) + "/" +  to_string(distance) << "\n";
  }

}