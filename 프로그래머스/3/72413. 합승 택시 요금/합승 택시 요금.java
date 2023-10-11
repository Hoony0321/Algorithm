import java.util.*;
class Solution {
    public int solution(int n, int s, int a, int b, int[][] fares) {
        int[][] dist = new int[n+1][n+1];
        int[][] next = new int[n+1][n+1];
        int INF = n * 100001;
        
        // dist & path 초기화
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                dist[i][j] = i == j ? 0 : INF;
                next[i][j] = -1;
            }
        }
        
        // fares 경로 적용
        for(int[] fare : fares){
            int u = fare[0]; int v = fare[1]; int w = fare[2];
            dist[u][v] = w;
            dist[v][u] = w;
        }
        
        // 플루이드-워샬 적용
        for(int k = 1; k <= n; k++){
            for(int i = 1; i <= n; i++){
                for(int j = 1; j <= n; j++){
                    if(i == j || i == k || k == j) continue;
                    if(dist[i][j] > dist[i][k] + dist[k][j]){
                        dist[i][j] = dist[i][k] + dist[k][j];
                        next[i][j] = k;
                    }
                    
                }
            }
        }
        
        int minFareSum = dist[s][a] + dist[s][b];
        
        // 최소 가격 구하기
        for(int i = 1; i <= n; i++){
            int fareSum = 0;
            
            // 갈 수 있는 길이 없는 경우
            if(dist[s][i] == INF || dist[i][a] == INF || dist[i][b] == INF) continue;
            
            // 경유지까지 같이 이동
            fareSum += dist[s][i];
            
            // 경유지에서 A,B 각각 이동
            fareSum += dist[i][a];
            fareSum += dist[i][b];
            
            // 최솟값 구하기
            minFareSum = Math.min(minFareSum, fareSum);
        }
        
        return minFareSum;
    }
}