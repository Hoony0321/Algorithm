//codeup_4051 : 시간외 근무 수당 - 정올1번문제
#include<iostream>
#include<vector>

using namespace std;

vector<vector<float>> workSchedule(5,vector<float>(2,0.0));

float CacluatingTime(float start, float end){
  float worktime = end - start;
  if(worktime - 1 > 4.0){return 4.0f;}
  if(worktime < 1.0) return 0.0;
  return worktime - 1.0;
  
  }

void CacluatingAllowance(vector<vector<float>> workSchedule){
  float totaltime = 0;
  for(auto elem : workSchedule){
    totaltime += CacluatingTime(elem[0], elem[1]);
  }
  int allowance = totaltime / 0.5 * 5000;
  if(totaltime >= 15.0){
    allowance = allowance * 0.95;
  }
  else if(totaltime <= 5.0){ 
    allowance = allowance * 1.05;
  }

  cout << allowance << endl;
}

int main(){
  for(auto& elem : workSchedule){
    for(auto& elem2: elem){
      cin >> elem2;
    }
  }

  CacluatingAllowance(workSchedule);

}
