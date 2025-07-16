import java.util.*;

class Solution {
    private int n;
    private int m;
    private String[] storage;
    private String[] requests;
    private int answer;
    
    public void processCrane(char request){
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(storage[i].charAt(j) == request){
                    storage[i] = storage[i].substring(0,j) + " " + storage[i].substring(j+1,m);
                    answer -= 1;
                }
            }
        }
    }
    
    public void processForklift(char request){
        String[] newStorage = new String[n+2];
        newStorage[0] = " ".repeat(m+2);
        newStorage[n+1] = " ".repeat(m+2);
        for(int i = 0; i < n; i++){
            newStorage[i+1] = " " + storage[i] + " ";
        }
        
        int[][] dxys = new int[][]{{0,1},{1,0},{0,-1},{-1,0}};
        boolean[][] visited = new boolean[n+2][m+2];
        Deque<int[]> deque = new ArrayDeque<>();
        deque.addFirst(new int[]{0,0});
        
        while(!deque.isEmpty()){
            int[] pos = deque.removeLast();
            int y = pos[0];
            int x = pos[1];
            if(visited[y][x]) continue;
            visited[y][x] = true;
            
            for(int[] dxy : dxys){
                int ny = y + dxy[0];
                int nx = x + dxy[1];
                
                if(ny < 0 || ny > n+1 || nx < 0 || nx > m+1) continue;
                if(visited[ny][nx]) continue;
                
                if(newStorage[ny].charAt(nx) == request){
                    newStorage[ny] = newStorage[ny].substring(0,nx) + "." + newStorage[ny].substring(nx+1,m+2);
                    continue;
                }
                if(newStorage[ny].charAt(nx) == ' '){
                    deque.addFirst(new int[]{ny,nx});
                }
            }   
        }
        
        for(int i = 1; i < n+1; i++){
            for(int j = 1; j < m+1; j++){
                if(newStorage[i].charAt(j) == '.'){
                    storage[i-1] = storage[i-1].substring(0,j-1) + " " + storage[i-1].substring(j,m);
                    answer -= 1;
                }
            }
        }        
    }
    
    
    
    public int solution(String[] storage, String[] requests) {
        this.storage = storage;
        this.requests = requests;
        this.n = storage.length;
        this.m = storage[0].length();
        this.answer = n * m;
        
        for(String request : requests){
            if(request.length() == 1){
                processForklift(request.charAt(0));
            }
            else{
                processCrane(request.charAt(0));
            }
        }
        
        for(String row : storage){
            System.out.println(row);
        }
        
        return answer;
    }
}