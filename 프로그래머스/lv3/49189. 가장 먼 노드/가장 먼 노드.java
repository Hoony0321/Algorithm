import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        List<List<Integer>> graph = new ArrayList<>();
        
        for(int i = 0; i < n; i++){
            graph.add(new ArrayList<>());
        }
        
        for(int[] item : edge){
            int u = item[0]; int v = item[1];
            graph.get(u-1).add(v-1);
            graph.get(v-1).add(u-1);
        }
        
        boolean[] visited = new boolean[n];
        
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);
        visited[0] = true;  // 시작 노드를 방문했다고 표시
        
        while(!queue.isEmpty()){
            int queueSize = queue.size();
            answer = 0;  // 이전 레벨의 노드 수를 초기화
            
            for(int i = 0; i < queueSize; i++){
                int u = queue.poll();
                
                answer++;
                
                for(int v : graph.get(u)){
                    if(visited[v]) continue;
                    visited[v] = true;  // 노드를 방문했다고 표시
                    queue.add(v);
                }
            }
        }
        
        return answer;
    }
}
