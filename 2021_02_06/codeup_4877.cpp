//codeup_4877 : 방 배정하기 - 2019정올 1번 문제
#include<iostream>
#include<vector>

using namespace std;

vector<int> list_rooms(3,0);
int students;

int main(){
  for(auto& elem : list_rooms){
    cin >> elem;
  }
  cin >> students;

  for(int i = 0; i <= students / list_rooms[2]; i++){
    for(int j = 0; j <= students/ list_rooms[1]; j++){
      for(int k = 0; k <= students/list_rooms[0]; k++){
        if(i * list_rooms[2] + j * list_rooms[1] + k * list_rooms[0] == students){
          cout << 1 << endl;
          return 0;
        }
      }
    }
  }
  cout << 0 << endl;
  return 0;
}