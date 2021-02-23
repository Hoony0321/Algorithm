#include<iostream>
#include<deque>
#include<algorithm>

using namespace std;

bool compare(pair<int,int> pair1, pair<int,int> pair2){
  if(pair1.second == pair2.second) return pair1.first < pair2.first;
  return pair1.second < pair2.second;
  
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL);
  
  int max_available = 0;
  int conferenceNum;
  cin >> conferenceNum;

  deque<pair<int,int>> schedule;

  for(int i = 0; i < conferenceNum; i++){
    bool find = false;
    pair<int,int> tempPair;
    cin >> tempPair.first >> tempPair.second;
    schedule.push_back(tempPair);
  }

  //정렬
  sort(schedule.begin(),schedule.end(),compare);

  
  int count = 0;
  int prev_start = 0;
  int prev_end = 0;
  for(deque<pair<int,int>>::iterator iter = schedule.begin(); iter != schedule.end(); iter++){
    int start = (*iter).first;
    int end = (*iter).second;
    if(prev_end <= start){
      count += 1;
      prev_start = start;
      prev_end = end;
    }
  }
  if(count > max_available) max_available = count;


  cout << max_available << "\n";
  

}