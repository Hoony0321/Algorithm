import java.util.*;
class Solution {
    public int[][] turnRight(int[][] board){
        int size = board.length;
        int[][] newBoard = new int[size][size];
        for(int i = 0; i < size; i ++){
            Arrays.fill(newBoard[i], 0);    
        }
        for(int i = 0; i < size; i++){
            for(int j = 0; j < size; j++){
                if(board[i][j] == 0) continue;
                newBoard[j][size-i-1] = 1;
            }
        }
        
        return newBoard;
    }
    
    public boolean isOpen(int[][] key, int[][] lock){
        int n = lock.length; int m = key.length;
        int size = m + (n-1) * 2;
        int[][] checkBoard = new int[size][size];
        for(int i = 0; i < size; i ++){
            Arrays.fill(checkBoard[i], 0);    
        }
        
        // key 값 넣기
        for(int i = 0; i < m; i++){
            for(int j = 0; j < m; j++){
                checkBoard[i+n-1][j+n-1] = key[i][j];
            }
        }
        
        // 보드 이동
        for(int i = 0; i < size-n+1; i++){
            for(int j = 0; j < size-n+1; j++){
              // 보드 체크
                boolean isAvailable = true;
                for(int p = 0; p < n; p++){
                    if(!isAvailable) break;
                    for(int q = 0; q < n; q++){
                        if(lock[p][q] == checkBoard[p+i][q+j]){ // 불가능한 경우
                            isAvailable = false;
                            break;
                        }
                    }
                }        
                if(isAvailable) return true;
            }
        }
        return false;
    }
    
    public boolean solution(int[][] key, int[][] lock) {
        boolean answer = false;
        
        
        for(int i = 0; i < 4; i++){
            if(isOpen(key, lock)){
                answer = true;
                break;
            }
            else{
                // 90도 회전
                key = turnRight(key);
            }
        }
        
        return answer;
    }
    
}