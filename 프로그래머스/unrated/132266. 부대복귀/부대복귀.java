import java.util.*;
class Solution {
    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        PriorityQueue<int[]> queue = new PriorityQueue<>((o1,o2) -> Integer.compare(o1[1], o2[1]));
        List<List<Integer>> edges = new ArrayList<>();
        int[] distMap = new int[n+1];
        
        for(int i = 0; i < n+1; i++){
            edges.add(new ArrayList<>());
        }
        
        for(int[] road : roads){
            edges.get(road[0]).add(road[1]);
            edges.get(road[1]).add(road[0]);
        }
        
        for(int i = 0; i < distMap.length; i++){
            distMap[i] = -1;
        }
        
        queue.add(new int[]{destination, 0});
        while(!queue.isEmpty()){
            int[] elem = queue.poll();
            int vertex = elem[0]; int dist = elem[1];
            
            if(distMap[vertex] != -1 && distMap[vertex] <= dist) continue;
            distMap[vertex] = dist;
            
            for(int vertex2 : edges.get(vertex)){
                int nDist = dist + 1;
                if(distMap[vertex2] == -1 || distMap[vertex2] > nDist){
                    queue.add(new int[]{vertex2, nDist});
                }
            }
        }
        
        int[] answer = new int[sources.length];
        for(int i = 0; i < sources.length; i++){
            answer[i] = distMap[sources[i]];
        }
        
        return answer;
    }
}