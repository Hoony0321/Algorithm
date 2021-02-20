#include<iostream>

using namespace std;

int N,M;
char paintWB[2] = {'W','B'};
char board[50][50];
int min_num = 64;


int CacluatingPaintingBlock(char baord_in[8][8]){
  //board[0][0] == 'W'인 경우
  int paint_start_W = 0;
  for(int i = 0; i < 8; i++){
    for(int j = 0; j < 8; j++){
      if(baord_in[i][j] != paintWB[(i+j)%2]){
        paint_start_W += 1;
      }
    }
  }
  //board[0][0] == 'B'인 경우
  int paint_start_B = 64 - paint_start_W;

  if(paint_start_W < paint_start_B) return paint_start_W;
  else return paint_start_B;
}

void Cacluating(int* startPoint){
  char tempBoard[8][8];
  for(int i = startPoint[0]; i < startPoint[0] + 8; i++){
    for(int j = startPoint[1]; j < startPoint[1] + 8; j++){
      tempBoard[i - startPoint[0]][j - startPoint[1]] = board[i][j];
    }
  }
  int required_painting = CacluatingPaintingBlock(tempBoard);
  if(min_num > required_painting) min_num = required_painting;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL);
  cin >> N >> M;

  
  for(int i = 0; i < N; i++){
    for(int j = 0; j < M; j++){
      cin >> board[i][j];
    }
  }

  int startPoint[2] = {0,0};

  for(int i = 0; i < N - 7; i++){
    for(int j = 0; j < M - 7; j++){
      startPoint[0] = i; startPoint[1] = j;
      Cacluating(startPoint);
    }
  }

  cout << min_num << "\n";



}