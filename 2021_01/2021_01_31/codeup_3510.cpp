#include<iostream>
#include<vector>

using namespace std;

int budget; //예산
int number_of_activity;
vector<int> activityCosts;
int min_remainBudget;
int min_activityCost;

void FindingMaxCost(int index,vector<bool> containActivities, int remainBudget){
  if(remainBudget < min_activityCost){ //남은 예산이 최저 활동비보다 작을 경우 바로 종료
    if(min_remainBudget > remainBudget) min_remainBudget = remainBudget;
    return; 
  }

  if(activityCosts[index] > remainBudget) {// 예산 초과로 종료
    if(min_remainBudget > remainBudget) min_remainBudget = remainBudget;
    return; 
  }
  

  containActivities[index] = true;
  remainBudget -= activityCosts[index];

  bool isLast = true;
  for(int i = 0; i < number_of_activity; i++){
    
    if(containActivities[i] == false){
      isLast = false;
      FindingMaxCost(i,containActivities,remainBudget);
    }
  
  }

   if(isLast == true){ // 모든 활동이 가능한 경우
      min_remainBudget = remainBudget;
      return;
    }

}

int main(){
  vector<bool> containActivities;

  cin >> budget >> number_of_activity;

  min_remainBudget = budget;
  min_activityCost = budget;

  activityCosts.resize(number_of_activity,0);
  containActivities.resize(number_of_activity, false);

  for(auto& elem : activityCosts){
    int cost;
    cin >> cost;
    if(cost < min_activityCost) min_activityCost = cost;
    elem = cost;
  }

  for(int i = 0; i < number_of_activity; i++){
    FindingMaxCost(i,containActivities,budget);
  }

  int result = budget - min_remainBudget;
  cout << result << endl;


}