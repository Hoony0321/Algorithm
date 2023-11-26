import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        int count = 0;
        List<List<Integer>> graph = new ArrayList<>();
        
        for(int i = 0; i < n+1; i++){
            graph.add(new ArrayList<>());
        }
        
        for(int[] e : edge){
            int u = e[0];
            int v = e[1];
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        
        boolean[] visited = new boolean[n+1];
        Queue<Integer> queue = new LinkedList<>();
        visited[1] = true;
        queue.add(1);
        
        while(!queue.isEmpty()){
            count = 0;
            int queueCurrentSize = queue.size();
            for(int i = 0; i < queueCurrentSize; i++){
                int node = queue.poll();
                count++;
                
                for(int near : graph.get(node)){
                    if(visited[near]) continue; // 이미 방문한 곳
                    
                    visited[near] = true;
                    queue.add(near);
                }
            }
        }
        
        return count;
    }
}