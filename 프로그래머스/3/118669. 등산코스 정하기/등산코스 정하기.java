import java.util.*;

class Solution {
    List<List<int[]>> graph;
    PriorityQueue<int[]> queue;
    boolean[] visited;
    int[] maxIntensities;
    
    private void initVariables(int n, int[] summits){
        graph = new ArrayList<>();
        for(int i = 0; i < n+1; i++){
            graph.add(new ArrayList<>());
        }
        
        visited = new boolean[n+1];
        maxIntensities = new int[n+1];
        Arrays.fill(maxIntensities, Integer.MAX_VALUE);
        queue = new PriorityQueue<>((e1,e2) -> e1[1] - e2[1]);
        Arrays.sort(summits);
    }
    
    private boolean isContain(int n, int[] array){
        for(int num : array){
            if(num == n) return true;
        }
        
        return false;
    }
    
    private void settingGraph(int[][] paths, int[] gates, int[] summits){
        for(int[] path : paths){
            int u = path[0];
            int v = path[1];
            int weight = path[2];
            
            // gate인 경우 - 나가는 간선만 존재
            // summit인 경우 - 들어오는 간선만 존재
            // 그 외 경우 - 나가는 간선 & 들어오는 간선 모두 존재
            if(isContain(u, gates) || isContain(v, summits)){
                graph.get(u).add(new int[]{v, weight});
            }
            else if(isContain(u, summits) || isContain(v, gates)){
                graph.get(v).add(new int[]{u, weight});
            }
            else{
                graph.get(u).add(new int[]{v, weight});
                graph.get(v).add(new int[]{u, weight});
            }
        }
    }
    
    private int getMinIntensitySummitNum(int[] summits){
        int minIntensity = Integer.MAX_VALUE;
        int minIntensitySummitNum = -1;
        for(int summit : summits){
            if(maxIntensities[summit] < minIntensity){
                minIntensitySummitNum = summit;
                minIntensity = maxIntensities[summit];
            }
        }
        
        return minIntensitySummitNum;
    }
    
    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        // 변수 초기화
        initVariables(n, summits);
        
        // graph 설정
        settingGraph(paths, gates, summits);
        
        // 시작 노드 삽입
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
            
            if(isContain(currentVertex, summits)) continue; // 산봉우리 경우 더 이상 진행 X
            
            for(int[] near : graph.get(currentVertex)){
                int nextVertex = near[0];
                int nextIntensity = near[1];
                int nextMaxIntensity = Math.max(currentMaxIntensity, nextIntensity);
                
                if(visited[nextVertex]) continue;
                if(isContain(nextVertex, gates)) continue; // 게이트는 중간 경유지 X
                if(maxIntensities[nextVertex] <= nextMaxIntensity) continue;
                
                maxIntensities[nextVertex] = nextMaxIntensity;
                queue.add(new int[]{nextVertex, nextMaxIntensity});
            }
        }
        
        int minIntensitySummitNum = getMinIntensitySummitNum(summits);
        return new int[]{minIntensitySummitNum, maxIntensities[minIntensitySummitNum]};
    }
}