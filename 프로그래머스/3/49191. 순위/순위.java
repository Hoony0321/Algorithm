import java.util.*;

class Solution {
    public int solution(int n, int[][] results) {
        
        int[][] graph = new int[n+1][n+1];
        for(int i = 1; i <= n; i++){
            Arrays.fill(graph[i],0);
        }
        
        for(int[] result : results){
            graph[result[0]][result[1]] = 1;
            graph[result[1]][result[0]] = -1;
        }
        
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                for(int k = 1; k <= n; k++){
                    if(i == j || j == k || i == k) continue;
                    if(graph[i][j] == 1 && graph[j][k] == 1){
                        graph[i][k] = 1;
                        graph[k][i] = -1;
                    }
                    else if(graph[i][j] == -1 && graph[j][k] == -1){
                        graph[i][k] = -1;
                        graph[k][i] = 1;
                    }
                }
            }
        }
        
        // for(int[] list : graph){
        //     for(int elem : list){
        //         System.out.print(elem);
        //         System.out.print(" ");
        //     }
        //     System.out.println();
        // }
        
        int answer = 0;
        for(int i = 1; i <= n; i++){
            boolean check = true;
            for(int j = 1; j <= n; j++){
                if(i != j && graph[i][j] == 0){
                    check = false;
                    break;
                }
            }
            if(check) answer++;
        }
        
        return answer;
    }
}