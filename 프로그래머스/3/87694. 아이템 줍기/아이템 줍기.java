import java.util.*;

class Solution {
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        // 초기 맵 세팅
        int[][] map = new int[102][102];
        for(int[] arr : map){
            Arrays.fill(arr, 0);
        }
        
        // rectangle 세팅
        for(int[] rect : rectangle){
            int x1 = rect[0];
            int y1 = rect[1];
            int x2 = rect[2];
            int y2 = rect[3];
            
            for(int i = y1 *2; i <= y2 * 2; i++){
                for(int j = x1 * 2; j <= x2 * 2; j++){
                    map[i][j] = 1;
                }
            }
        }
        
        // 테두리 부분만 남기기
        boolean[][] checked = new boolean[101][101];
        for(int i = 1; i <= 100; i++){
            for(int j = 1; j <= 100; j++){
                if(map[i][j] == 0) continue;
                if(map[i-1][j-1] == 0 || map[i-1][j] == 0 || map[i-1][j+1] == 0 ||
                   map[i+1][j-1] == 0 || map[i+1][j] == 0 || map[i+1][j+1] == 0 ||
                   map[i][j-1] == 0 || map[i][j+1] == 0) continue;
                
                checked[i][j] = true;
            }
        }  
        for(int i = 1; i <= 100; i++){
            for(int j = 1; j <= 100; j++){
                if(checked[i][j]){
                    map[i][j] = 0;
                }
            }
        }
        
        // 최단 거리 구하기
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{characterY * 2, characterX * 2});
        
        int step = 0;
        boolean[][] visited = new boolean[101][101];
        visited[characterY * 2][characterX * 2] = true;
        int[][] dxys = new int[][]{{0,1}, {1,0}, {0,-1}, {-1,0}};
        while(!queue.isEmpty()){
            int queueSize = queue.size();
            for(int i = 0; i < queueSize; i++){
                int[] elem = queue.poll();
                int y = elem[0];
                int x = elem[1];
                
                if(x == itemX * 2 && y == itemY * 2){
                    queue.clear();
                    break;
                }
                
                for(int[] dxy : dxys){
                    int ny = y + dxy[0];
                    int nx = x + dxy[1];
                    
                    if(ny < 0 || ny > 100 || nx < 0 || nx > 100) continue; // 맵 범위 벗어남
                    if(visited[ny][nx]) continue; // 이미 방문한 곳
                    if(map[ny][nx] == 0) continue; // 테두리가 아님
                    
                    visited[y][x] = true;
                    queue.add(new int[]{ny,nx});
                }
            }
            step++;
        }
        
        
        return (step-1)/2;
    }
}