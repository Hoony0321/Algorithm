import java.util.*;

class Solution {
    
    private boolean isGate(int vertex, int[] gates){
        for(int n : gates){
            if(vertex == n) return true;
        }
        
        return false;
    }
    
    private boolean isSummit(int vertex, int[] summits){
        for(int n : summits){
            if(vertex == n) return true;
        }
        
        return false;
    }
    
    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        Arrays.sort(summits);
        // graph 설정
        List<List<int[]>> graph = new ArrayList<>();
        for(int i = 0; i < n+1; i++){
            graph.add(new ArrayList<>());
        }
        
        for(int[] path : paths){
            int u = path[0];
            int v = path[1];
            int weight = path[2];
            
            // gate인 경우 - 나가는 간선만 존재
            // summit인 경우 - 들어오는 간선만 존재
            // 그 외 경우 - 나가는 간선 & 들어오는 간선 모두 존재
            if(isGate(u, gates) || isSummit(v, summits)){
                graph.get(u).add(new int[]{v, weight});
            }
            else if(isSummit(u, summits) || isGate(v, gates)){
                graph.get(v).add(new int[]{u, weight});
            }
            else{
                graph.get(u).add(new int[]{v, weight});
                graph.get(v).add(new int[]{u, weight});
            }
        }
        
        // visited 설정
        boolean[] visited = new boolean[n+1];
        
        // dist 설정
        int[] maxIntensities = new int[n+1];
        Arrays.fill(maxIntensities, Integer.MAX_VALUE);
        
        // queue 설정
        PriorityQueue<int[]> queue = new PriorityQueue<>((e1,e2) -> e1[1] - e2[1]);
        
        for(int gate : gates){
            maxIntensities[gate] = 0;
            queue.add(new int[]{gate, 0});
        }
        
        // 다익스트라 알고리즘
        while(!queue.isEmpty()){
            int[] elem = queue.poll();
            int currentVertex = elem[0];
            int currentMaxIntensity = elem[1];
            
            if(visited[currentVertex]) continue;
            visited[currentVertex] = true;
            
            if(isSummit(currentVertex, summits)) continue; // 산봉우리 경우 더 이상 진행 X
            
            for(int[] near : graph.get(currentVertex)){
                int nextVertex = near[0];
                int nextIntensity = near[1];
                int nextMaxIntensity = Math.max(currentMaxIntensity, nextIntensity);
                
                if(visited[nextVertex]) continue;
                if(isGate(nextVertex, gates)) continue; // 게이트는 중간 경유지 X
                if(maxIntensities[nextVertex] <= nextMaxIntensity) continue;
                
                maxIntensities[nextVertex] = nextMaxIntensity;
                queue.add(new int[]{nextVertex, nextMaxIntensity});
            }
        }
        
        int minIntensity = Integer.MAX_VALUE;
        int minIntensitySummitNum = -1;
        for(int summit : summits){
            if(maxIntensities[summit] < minIntensity){
                minIntensitySummitNum = summit;
                minIntensity = maxIntensities[summit];
            }
        }
        
        
        return new int[]{minIntensitySummitNum, minIntensity};
    }
}