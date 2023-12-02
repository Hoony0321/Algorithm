import java.util.*;

class Solution {
    
    class Node {
        int id;
        Node root;
        
        public Node(int id){
            this.id = id;
            root = this;
        }
        
        public Node getRoot(){
            Node node = root;
            while(node.root != node){
                node = node.root;
            }
            
            this.root = node; // update root
            return node;
        }
        
        public void union(Node otherNode){
            Node rootNode1 = this.getRoot();
            Node rootNode2 = otherNode.getRoot();
            
            // id가 작은 쪽으로 병합
            if(rootNode1.id < rootNode2.id){
                rootNode2.root = rootNode1;
            }
            
            if(rootNode1.id > rootNode2.id){
                rootNode1.root = rootNode2;
            }
        }
    }
    
    public int solution(int n, int[][] computers) {
        // initialize graph
        Node[] graph = new Node[n];
        for(int i = 0; i < n; i++){
            graph[i] = new Node(i);
        }
        
        // set graph
        for(int u = 0; u < n; u++){
            for(int v = 0; v < n; v++){
                if(computers[u][v] == 1) graph[u].union(graph[v]);
            }
        }
        
        // get number of network
        Set<Node> networkRoots = new HashSet<>();
        for(Node node : graph){
            networkRoots.add(node.getRoot());    
        }
        
        return networkRoots.size();
    }
}