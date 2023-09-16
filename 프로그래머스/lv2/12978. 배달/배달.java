import java.util.*;

class Solution {
    public int solution(int N, int[][] road, int K) {
        int answer = 0;
        List<List<int[]>> graph = new ArrayList<>();
        for(int i = 0; i < N+1; i++){
            graph.add(new ArrayList<>());
        }
        
        for(int[] edge : road){
            int u = edge[0], v = edge[1], w = edge[2];
            graph.get(u).add(new int[]{v,w});
            graph.get(v).add(new int[]{u,w});
        }
        
        int[] dist = findMinDist(1, graph);
        
        for(int i = 0; i < dist.length; i++){
            if(dist[i] <= K){
                answer += 1;
            }
        }

        return answer;
    }
    
    public int[] findMinDist(int start, List<List<int[]>> graph){
        int[] dist = new int[graph.size()];
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1,o2) -> Integer.compare(o1[1], o2[1]));
        
        for(int i = 0; i < dist.length; i++){
            dist[i] = Integer.MAX_VALUE;
        }
        dist[start] = 0;
        pq.add(new int[]{start, 0});
        
        while(!pq.isEmpty()){
            int[] elem = pq.poll();
            int u = elem[0]; int d = elem[1];
            
            if(d > dist[u]) continue;
            
            for(int[] near : graph.get(u)){
                int v = near[0]; int w = near[1];
                int nd = d + w;
                
                if(dist[v] > nd){
                    dist[v] = nd;
                    pq.add(new int[]{v,nd});
                }
            }
        }
        
        return dist;
    }
}