#include<iostream>

using namespace std;

int map[100][100] = {0,}

void DragonCurb(int y, int x, int d, int g){
  //0세대
  map[0][0] = 1; map[0][1] = 1;
  //1세대
  DragonCurb(y,x,d,0);
      
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);


}