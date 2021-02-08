//codeup_4040 : 펜션 - 그리디(어려움)
#include<iostream>
#include<vector>
#include<string>
using namespace std;

int period;
int rooms;
int result = 0 ;
vector<int> request(2,0);
vector<string> reserveList;
vector<int> availableroom;

vector<int> FindingAvailableRoom(int start){
  
  int count = 0;
  for(auto elem : reserveList[start]){
    if(elem == 'O') availableroom.push_back(count);
    count += 1;
  }
  return availableroom;
}

int FindingHowLongUse(vector<int> availableroom, int start, int end){
  for(int i = start+1; i <= end; i++){
    for(int j = 0; j < availableroom.size(); j++){
      if(reserveList[i][availableroom[j]] == 'X'){
        availableroom.erase(availableroom.begin() + j-1);
        start = i;
      }
      cout << availableroom.size() << endl;
    }
  }
  cout << start  << " here " << endl;
  return start;
}

void selectRoom(int index, int start,int end){
  vector<int> availableroom = FindingAvailableRoom(start);
  cout << "here" << endl;
  if(availableroom.size() == 0) result  = -1;
  
  start = FindingHowLongUse(availableroom,start,end);

  if(start >= end-1){result = index +1;}

  selectRoom(index+1, start, end);
  availableroom.clear();
}

int main(){
  cin >> period >> rooms;
  for(int i = 0 ; i < period; i++){
    string input;
    cin >> input;
    reserveList.push_back(input);
  }

  cin >> request[0]>> request[1];

  selectRoom(0,request[0]-1,request[1]-1);
  cout << result << endl;
  
  
}
