import java.util.*;

class Solution {
    int maxVisitNum = 0;
    
    private void dfs(boolean[] visited, int visitNum, int k, int[][] dungeons){
        maxVisitNum = Math.max(maxVisitNum, visitNum);
        
        for(int i = 0; i < visited.length; i++){
            if(visited[i]) continue; // 이미 방문한 곳
            if(k < dungeons[i][0]) continue; // 최소 피로도 조건에 부합X
            
            visited[i] = true;
            dfs(visited, visitNum + 1, k - dungeons[i][1], dungeons);
            visited[i] = false;
        }
    }
    
    public int solution(int k, int[][] dungeons) {
        boolean[] visited = new boolean[dungeons.length];
        dfs(visited, 0, k, dungeons);
        
        return maxVisitNum;
    }
}