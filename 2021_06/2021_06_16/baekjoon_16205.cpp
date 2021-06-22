#include<iostream>
#include<algorithm>
#include<string>
#include<vector>

using namespace std;

int num;
string str;
vector<string> words;

void separateCase1(){
  int startIndex = 0;
  int endIndex = 0;
  for(int i = 0; i < str.length(); i++){
    if(isupper(str[i])){
      endIndex = i-1;
      string temp = str.substr(startIndex,endIndex - startIndex + 1);
      words.push_back(temp);
      startIndex = endIndex + 1;
    }
    if(i == str.size() - 1){
      words.push_back(str.substr(startIndex));
    }
  }
}

void separateCase2(){
  bool check = false;
  int startIndex = 0;
  vector<int> vec;
  while(str.find("_",startIndex) != string::npos){
    int index = str.find("_",startIndex);
    vec.push_back(index);
    startIndex = index + 1;
  }

  startIndex = 0;
  for(int i = 0; i < vec.size(); i++){
    words.push_back(str.substr(startIndex,vec[i] - startIndex));
    startIndex = vec[i] + 1;
  }

  words.push_back(str.substr(startIndex));
  
}

void separateCase3(){
  int startIndex = 0;
  int endIndex = 0;
  for(int i = 1; i < str.length(); i++){
    if(isupper(str[i])){
      endIndex = i-1;
      string temp = str.substr(startIndex,endIndex - startIndex + 1);
      words.push_back(temp);
      startIndex = endIndex + 1;
    }
    if(i == str.size() - 1){
      words.push_back(str.substr(startIndex));
    }
  }

  if(str.size() == 1) words.push_back(str);
}

void separateWord(){
  switch(num){
    case 1:
      separateCase1();;
      break;
    case 2:
      separateCase2();
      break;
    case 3:
      separateCase3();
      break;
  }
}

void returnToWord(){
  string outPut = "";

  words[0][0] = tolower(words[0][0]);
  outPut += words[0];
  for(int i = 1; i < words.size(); i++){
    words[i][0] = toupper(words[i][0]);
    outPut += words[i];
  }

  cout << outPut << "\n";
  outPut = "";

  words[0][0] = tolower(words[0][0]);
  outPut += words[0];
  for(int i = 1; i < words.size(); i++){
    outPut += "_";
    words[i][0] = tolower(words[i][0]);
    outPut += words[i];
  }

  cout << outPut << "\n";
  outPut = "";

  words[0][0] = toupper(words[0][0]);
  outPut += words[0];
  for(int i = 1; i < words.size(); i++){
    words[i][0] = toupper(words[i][0]);
    outPut += words[i];
  }

  cout << outPut << "\n";

}

int main(){
  cin >> num >> str;
  separateWord();
  returnToWord();
}