//baekjonn_19844_단어 개수 세기
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

string sentance;
vector<string> sentance_split;
vector<int> split_point;

void SplitSentance1(){
  int start_pos1 = 0;
  int start_pos2 = 0;
  while(sentance.find(" ",start_pos1) != string::npos){
    start_pos1 = sentance.find(" ",start_pos1) + 1;
    split_point.push_back(start_pos1 - 1);
  }
  while(sentance.find("-",start_pos2) != string::npos){
    start_pos2 = sentance.find("-",start_pos2) + 1;
    split_point.push_back(start_pos2 - 1);
  }

  sort(split_point.begin(), split_point.end());

  int start_pos3 = 0;
  for(int i = 0; i < split_point.size(); i++){
    string str = sentance.substr(start_pos3, split_point[i] - start_pos3);
    sentance_split.push_back(str);
    start_pos3 = split_point[i] + 1;
  }
  sentance_split.push_back(sentance.substr(split_point[split_point.size()-1]+1));

}

int main(){

  getline(cin,sentance);

  SplitSentance1();
  

  
  
  

}
