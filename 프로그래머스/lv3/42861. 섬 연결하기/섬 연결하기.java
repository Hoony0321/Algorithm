import java.util.*;

class Solution {
    public int solution(int n, int[][] costs) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        List<List<int[]>> edges = new ArrayList<>();
        for(int i = 0; i < n; i++){
            edges.add(new ArrayList<>());
        }
        
        for(int[] cost : costs){
            edges.get(cost[0]).add(new int[]{cost[1], cost[2]});
            edges.get(cost[1]).add(new int[]{cost[0], cost[2]});
        }
        
        PriorityQueue<int[]> queue = new PriorityQueue<>((o1,o2) -> o1[1] - o2[1]);
        
        visited[0] = true;
        for(int[] edge : edges.get(0)){
            queue.add(edge);
        }
        
        while(!queue.isEmpty()){
            int[] elem = queue.poll();
            int vertex = elem[0]; int cost = elem[1];
            
            if(visited[vertex]) continue; // 이미 방문한 경우는 패스
            visited[vertex] = true;
            answer += cost;
            
            for(int[] edge : edges.get(vertex)){
                if(visited[edge[0]]) continue;
                queue.add(edge);
            }
        }
        
        return answer;
    }
}