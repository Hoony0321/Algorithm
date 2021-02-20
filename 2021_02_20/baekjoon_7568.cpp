#include<iostream>

using namespace std;

int main(){
  ios_base::sync_with_stdio(false); cin.tie(NULL);
  int person;
  cin >> person;

  int* compareList = new int[person];
  int personalInfo[50][2];

  for(int i = 0; i < person; i++){
    cin >> personalInfo[i][0] >> personalInfo[i][1];
  }

  for(int i = 0; i < person-1; i++){
    for(int j = i+1; j < person; j++){
      if(personalInfo[i][0] < personalInfo[j][0] && personalInfo[i][1] < personalInfo[j][1]){
        compareList[i] += 1;
      }
      else if(personalInfo[i][0] > personalInfo[j][0] && personalInfo[i][1] > personalInfo[j][1]){
        compareList[j] += 1;
      }
    }
  }

  for(int i = 0; i < person; i++){
    cout << compareList[i] +1 << " ";
  }
  cout << "\n";
  
  

  delete[] compareList;
}