import java.util.*;

class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int[][] map = new int[n+2][m+2]; // padding 추가한 map
        
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= m; j++){
                map[i][j] = 0;
            }
        }
        for(int[] puddle : puddles){
            map[puddle[1]][puddle[0]] = -1;
        }
        
        map[1][1] = 1;
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= m; j++){
                if(map[i][j] == -1) continue;
                if(map[i-1][j] != -1) map[i][j] += map[i-1][j];
                if(map[i][j-1] != -1) map[i][j] += map[i][j-1];
                map[i][j] %= 1000000007;
            }
        }
        
        return map[n][m];
    }
}