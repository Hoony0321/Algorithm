//codeup_3501 : RGB 거리 (Small) - 탐색기반설계

#include <iostream>
#include <vector>

using namespace std;

int minimumPrice = 10000000;
int number_of_house;
vector<vector<int>> prices;
enum COLOR {RED,GREEN,BLUE,LAST};

int PaintingHouse(int house, COLOR color){
  return prices[house][color];
}

void FindingMinimumPrice(int index, COLOR cur_color, int total_price){
  if(total_price >= minimumPrice) return;
  if(index == number_of_house){
    if(total_price < minimumPrice) minimumPrice = total_price;
    return;
  }

  int add_price;

  for(int colorInt = RED; colorInt != LAST; colorInt++){
    COLOR color = static_cast<COLOR>(colorInt);

    if(color != cur_color){
      add_price = PaintingHouse(index,color);
      FindingMinimumPrice(index+1, color, total_price + add_price);
    }
  }
  
}



int main(){
  cin >> number_of_house;
  prices.resize(number_of_house);
  int price_to_color;
  for(int i = 0; i < number_of_house; i++){
    for(int j = 0; j < 3; j++){
      cin >> price_to_color;
      prices[i].push_back(price_to_color);
    }
  }
  FindingMinimumPrice(1, RED, prices[0][RED]);
  FindingMinimumPrice(1, GREEN, prices[0][GREEN]);
  FindingMinimumPrice(1, BLUE, prices[0][BLUE]);

  cout << minimumPrice << endl;
  
}