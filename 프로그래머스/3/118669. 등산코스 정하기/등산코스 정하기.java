import java.util.*;

class Solution {
    
    public boolean contains(int[] array, int value){
        for(int num : array){
            if(value == num) return true;
        }
        
        return false;
    }
    
    public boolean isVisitedAllSummits(int[] summits, boolean[] visited){
        for(int summit : summits){
            if(!visited[summit]) return false;
        }
        
        return true;
    }
    
    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        List<List<int[]>> graph = new ArrayList<>();
        Arrays.sort(summits);
        
        for(int i = 0; i < n+1; i++){
            graph.add(new ArrayList<>());
        }
        
        for(int[] path : paths){
            int u = path[0];
            int v = path[1];
            int time = path[2];
            
            if(contains(gates, u) || contains(summits, v)){
                graph.get(u).add(new int[]{v, time});    
            }
            else if(contains(gates, v) || contains(summits, u)){
                graph.get(v).add(new int[]{u, time});    
            } else {
                graph.get(u).add(new int[]{v, time});
                graph.get(v).add(new int[]{u, time});    
            }
        }
        
        PriorityQueue<int[]> queue = new PriorityQueue<>((e1,e2) -> e1[1] - e2[1]);
        
        boolean[] visited = new boolean[n+1];
        int[] intensities = new int[n+1];
        Arrays.fill(intensities, Integer.MAX_VALUE);
        
        // 각 gate에서 산봉우리 지점까지 최단 거리 구하기.
        for(int gate : gates){
            intensities[gate] = 0;
            queue.add(new int[]{gate,0});
        }
        
        while(!queue.isEmpty()){
            if(isVisitedAllSummits(summits, visited)) break;
            int[] elem = queue.poll();
            int vertex = elem[0];
            int curIntensity = elem[1];

            if(visited[vertex]) continue;
            visited[vertex] = true;
            
            for(int[] next : graph.get(vertex)){
                if(visited[next[0]]) continue;
                
                int nextIntensity = Math.max(curIntensity, next[1]);
                if(nextIntensity < intensities[next[0]]){
                    intensities[next[0]] = nextIntensity;    
                    queue.add(new int[]{next[0], nextIntensity});
                }
            }
        }
        
        int[] answer = new int[]{-1, Integer.MAX_VALUE};
        for(int summit : summits){
            if(answer[1] > intensities[summit]){
                answer[0] = summit;
                answer[1] = intensities[summit];
            }
        }
        
        return answer;
    }
}