#include<iostream>
#include<vector>

using namespace std;




int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  int city_num;
  cin >> city_num;
  
  vector<long> road(city_num-1);
  vector<long> city_oil(city_num);
  
  for(int i = 0; i < city_num-1; i++){
    cin >> road[i];
  }
  for(int i = 0; i < city_num; i++){
    cin >> city_oil[i];
  }

  for(int i = 0; i < city_oil.size()-1; i++){
    if(city_oil[i] < city_oil[i+1]) city_oil[i+1] = city_oil[i];
  }

  long sum =0;
  for(int i = 0; i < road.size(); i++){
    sum += road[i] * city_oil[i];
  }

  cout << sum << "\n";

}