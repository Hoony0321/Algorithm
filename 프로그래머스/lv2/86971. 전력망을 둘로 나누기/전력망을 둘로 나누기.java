import java.util.*;

class Solution {
    int answer = 100;
    Set<Integer> visited = new HashSet<>();
    Map<Integer, Set<Integer>> tree = new HashMap<>();
    
    public int solution(int n, int[][] wires) {
        
        for(int[] wire : wires){
            if(!tree.containsKey(wire[0])) tree.put(wire[0], new HashSet<>());
            if(!tree.containsKey(wire[1])) tree.put(wire[1], new HashSet<>());
            tree.get(wire[0]).add(wire[1]);
            tree.get(wire[1]).add(wire[0]);
        }
        
        treeTravel(wires[0][0]);
        return answer;
    }
    
    public int treeTravel(int root){
        if(visited.contains(root)) return 0;
        visited.add(root);
        
        int count = 1;
        
        for(int child : tree.get(root)){
            count += treeTravel(child);
        }
        
        int otherCount = tree.keySet().size() - count;
        answer = Math.min(answer, Math.abs(otherCount-count));
        
        return count;
    }
}