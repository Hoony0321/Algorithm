#include <iostream>
#include<vector>

using namespace std;

//codeup_2608 : 동아리 회장 선거 - depth first search(dfs)

int number_of_voter;5

void FindingAllCase(int index, vector<char> currentVote){
  if(index == number_of_voter){
    for(auto elem : currentVote){
      cout << elem;
    }
    cout << endl;
    return;
  }

  currentVote[index] = 'O';
  FindingAllCase(index+1, currentVote);

  currentVote[index] = 'X';
  FindingAllCase(index+1, currentVote);
  
}

int main() {
  cin >> number_of_voter;
  vector<char> currentVote(number_of_voter,' ');

  FindingAllCase(0,currentVote);

}