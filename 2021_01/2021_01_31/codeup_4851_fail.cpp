#include<iostream>
#include<vector>

using namespace std;

//codeup_4851 : 동전 게임 - backtracking? not sure

int round;
int number_of_check;
vector<vector<int>> score_cases;

int main(){
  cin >> round >> number_of_check;
  score_cases.resize(number_of_check);
  for(auto& elem : score_cases){
    elem.resize(2,0);
  }

  for(int i = 0; i < number_of_check; i++){
    cin >> score_cases[i][0] >> score_cases[i][1];
  }

}

