import java.util.*;

class Solution {
    public int solution(int[][] board) {
        int boardSize = board.length;
        int[][][] visited = new int[boardSize][boardSize][4];
        int[][] dirList = new int[][]{{1,0}, {0,1}, {-1,0}, {0,-1}}; // 아래, 오른쪽, 위, 왼쪽
        
        for(int i = 0; i < boardSize; i++){
            for(int j = 0; j < boardSize; j++){
                for(int k = 0; k < 4; k++){
                    visited[i][j][k] = Integer.MAX_VALUE;
                }
            }
        }
        
        PriorityQueue<int[]> queue = new PriorityQueue<>(new Comparator<int[]>(){
            @Override
            public int compare(int[] o1, int[] o2){
                return o1[2] - o2[2];
            }
        });
        
        for(int i = 0; i < 4; i++){
            visited[0][0][i] = 0;
        }
        
        if(board[0][1] != 1) queue.add(new int[]{0,1,100,1});
        if(board[1][0] != 1) queue.add(new int[]{1,0,100,0});
        
        while(!queue.isEmpty()){
            int[] elem = queue.poll();
            int y = elem[0]; int x = elem[1]; int cost = elem[2]; int dir = elem[3];
            
            if(visited[y][x][dir] <= cost) continue;
            visited[y][x][dir] = cost;
            
            if(x == boardSize-1 && y == boardSize-1) continue;
            
            for(int i = 0; i < 4; i++){
                if(Math.abs(i - dir) == 2) continue; // 이전에 왔던 방향 가지치기
                int ny = y + dirList[i][0]; int nx = x + dirList[i][1];
                int nCost = cost + ((i == dir) ? 100 : 600);
                
                if(ny < 0 || ny >= boardSize || nx < 0 || nx >= boardSize) continue; // 맵 범위 벗어남
                if(board[ny][nx] == 1) continue; // 벽은 못 지나감
                if(visited[ny][nx][i] <= nCost) continue; // 이미 지나간 경로
                queue.add(new int[]{ny,nx,nCost,i});
            }
        }
        
        
        return Arrays.stream(visited[boardSize-1][boardSize-1]).min().getAsInt();
    }
}