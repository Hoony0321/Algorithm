#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

//codeup_3321 : 최고의 피자 - greed method

int dough_price;
int topping_price;
int number_of_topping;
vector<int> topping_calories;
int dough_calorie;

double dough_calories_per_dollar;
vector<double> topping_calories_per_dollar;

vector<bool> usedTopping;

double currentPrice = 0.0;
double currentCalories = 0.0;
double currentCalories_perDollar = 0.0;

void AddingTopping(int index);
int FindingBestCalorieTopping();
void FindingBestPizza();

int main(){
  cin >> number_of_topping;
  usedTopping.resize(number_of_topping,false);
  cin >> dough_price >> topping_price;

  cin >> dough_calorie;

  int tmp_calorie; // instance variable for getting topping calorie
  for(int i = 0; i < number_of_topping; i++){
    cin >> tmp_calorie;
    topping_calories.push_back(tmp_calorie);
  }

  dough_calories_per_dollar = double(dough_calorie) / double(dough_price);
  for(int i = 0; i < number_of_topping; i++){
    topping_calories_per_dollar.push_back(
      double(topping_calories[i]) / double(topping_price)
    );
  }




  currentCalories = dough_calorie;
  currentPrice = dough_price;
  currentCalories_perDollar = dough_calories_per_dollar;
  FindingBestPizza();
  cout << floor(currentCalories_perDollar) << endl;
}

void AddingTopping(int index){
  usedTopping[index] = true;
  currentCalories += topping_calories[index];
  currentPrice += topping_price;
  currentCalories_perDollar = currentCalories / currentPrice;
}

int FindingBestCalorieTopping(){
  int max_calorie = 0;
  int index = -1;
  for(int i = 0; i < number_of_topping; i++){
    if(usedTopping[i] == false){
      if(max_calorie < topping_calories_per_dollar[i]){
        max_calorie = topping_calories_per_dollar[i];
        index = i;
      }
    }
  }
  if(max_calorie <= currentCalories_perDollar) index = -1;

  return index;
}

void FindingBestPizza(){
  
  int bestTopping = FindingBestCalorieTopping();
  if(bestTopping == -1){ return; }

  AddingTopping(bestTopping);
  FindingBestPizza();
}