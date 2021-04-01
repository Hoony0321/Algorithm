//codeup_4011 : 생년월일 출력 - 정올1번문제

#include<iostream>
#include<string>

using namespace std;

string input;

void print(string str1, int num){
  string year;
  char gender;
  switch(num){
    case 1:
      year = "19";
      gender = 'M';
      break;
    case 2:
      year = "19";
      gender = 'F';
      break;
    case 3:
      year = "00";
      gender = 'M';
      break;
    case 4:
      year = "00";
      gender = 'F';
      break;
  }

  cout << year + str1.substr(0,2) 
   + "/" + str1.substr(2,2)
   + "/" + str1.substr(4,2)
   + " " + gender
  << endl;
  
}

int main(){
  cin >> input;
  int pos = input.find("-");
  string str1 = input.substr(0,pos);
  int num = input[pos+1] - '0';
  
  print(str1, num);

}