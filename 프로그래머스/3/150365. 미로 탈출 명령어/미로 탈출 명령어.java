import java.util.*;

class Solution {
    char[] dirs;
    int[][] dxys;
    int[][] map;
    List<Character> shortestPath = new ArrayList<>();
    
    int targetSize;
    int targetY;
    int targetX;
    
    public void dfs(int y, int x, List<Character> path){
        if(shortestPath.size() != 0) return; // 정답을 구한 경우
        
        if(path.size() == targetSize && y == targetY && x == targetX){
            shortestPath = path;
            return;
        }
        
        for(int i = 0; i < 4; i++){
            char dir = dirs[i];
            int ny = y + dxys[i][0];
            int nx = x + dxys[i][1];
            int remainPath = Math.abs(targetY - ny) + Math.abs(targetX - nx);
            int remainStep = targetSize - (path.size() + 1);
            
            if(map[ny][nx] == -1) continue; // 맵 범위 벗어난 경우
            if(remainPath > remainStep) continue; // 남은 최단 거리가 갈 수 있는 거리보다 긴 경우
            if((remainStep - remainPath) % 2 != 0) continue; // 남은 스텝이 짝수가 아닌 경우

            List<Character> nPath = new ArrayList<>(path);
            nPath.add(dir);
            dfs(ny, nx, nPath);
        }
        
    }
    
    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        String answer = "";
        
        map = new int[n+2][m+2];
        for(int i = 0; i < n+2; i++){
            for(int j = 0; j < m+2; j++){
                if(i < 1 || i > n || j < 1 || j > m){
                    map[i][j] = -1;
                }
            }
        }
        
        targetSize = k;
        targetY = r;
        targetX = c;
        
        dirs = new char[]{'d', 'l', 'r', 'u'};
        dxys = new int[][]{{1,0}, {0,-1}, {0,1}, {-1,0}};
        
        dfs(x,y,new ArrayList<>());
        
        if(shortestPath.size() == 0){
            return "impossible";
        }
        
        for(char path : shortestPath){
            answer += path;
        }
        
        return answer;
    }
}