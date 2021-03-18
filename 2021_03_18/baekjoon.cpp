#include<iostream>
#include<cmath>
#include<deque>
using namespace std;

void SpinningGear(int number, int direction, deque<int>* gears){
  bool spin_right = false;
  bool spin_left = false;

  //왼쪽
  if(number-1 >= 0){
    if(gears[number-1][2] != gears[number][6]) spin_left = true;;
  }
  //오른쪽
  if(number+1 <= 7){
    if(gears[number+1][6] != gears[number][2]) spin_right = true;
  }


  //자신
  if(direction == 1){ //시계방향  
    int element_back = gears[number].back();
    gears[number].pop_back();
    gears[number].push_front(element_back);
  }
  else{
    int element_front = gears[number].front();
    gears[number].pop_front();
    gears[number].push_back(element_front);
  }


  //왼쪽
  if(spin_left){SpinningGear(number-1,direction==1?-1:1,gears);}
  //오른쪽
  if(spin_right){SpinningGear(number+1,direction==1?-1:1,gears);}

}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  deque<int> gears[4];

  
  //초기 상태 입력
  for(int i = 0; i < 4; i++){
    for(int j = 0; j < 8; j++){
      char inputVal;
      cin >> inputVal;
      gears[i].push_back(inputVal - '0');
    }
  }

  int spin;
  cin >> spin;

  //실행
  for(int i = 0; i < spin; i++){
    int number,direction;
    cin >> number >> direction;

    SpinningGear(number-1, direction, gears);
  }

  //결과
  int point = 0;
  for(int i = 0; i < 4; i++){
    point += gears[i][0] * pow(2,i);
  }

  cout << point << "\n";




}