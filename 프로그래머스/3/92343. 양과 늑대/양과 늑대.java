import java.util.*;

class Solution {
    int maxSheepNum = 0;
    
    class Node {
        int id;
        int type; // 0 - 양 & 1 - 늑대
        Node leftChild;
        Node rightChild;
        
        public Node(int id, int type){
            this.id = id;
            this.type = type;
            this.leftChild = null;
            this.rightChild = null;
        }
        
        public void addChild(Node child){
            if(this.leftChild != null){
                this.rightChild = child;
            }
            
            if(this.leftChild == null){
                this.leftChild = child;
            }
        }
        
        public String toString(){
            return Integer.toString(id);
        }
    }
    
    public void dfs(List<Node> nearNodes, int sheepNum, int wolfNum){
        if(sheepNum != 0 && wolfNum >= sheepNum){ return; }
        maxSheepNum = Math.max(maxSheepNum, sheepNum);
        
        if(nearNodes.isEmpty()){ // 종료 조건
            return;
        }
        
        int nearNodeSize = nearNodes.size();
        for(int i = 0; i < nearNodeSize; i++){
            Node node = nearNodes.get(i);
            // System.out.println(nearNodes);
            nearNodes.remove(node);
            
            // 자식 노드 nextNearNodes에 추가
            if(node.leftChild != null){
                nearNodes.add(node.leftChild);
            }
            if(node.rightChild != null){
                nearNodes.add(node.rightChild);
            }
            
            dfs(nearNodes, sheepNum + (node.type == 0 ? 1 : 0), wolfNum + (node.type == 1 ? 1 : 0));
            
            // 자식 노드 nextNearNodes에 삭제
            if(node.leftChild != null){
                nearNodes.remove(node.leftChild);
            }
            if(node.rightChild != null){
                nearNodes.remove(node.rightChild);
            }

            nearNodes.add(i, node);
        }
    }
    
    public int solution(int[] info, int[][] edges) {
        // nodes 초기화
        List<Node> nodes = new ArrayList<>();
        for(int i = 0; i < info.length; i++){
            nodes.add(new Node(i, info[i]));
        }
        
        // 노드 간 edge 연결
        for(int[] edge : edges){
            Node parent = nodes.get(edge[0]);
            Node child = nodes.get(edge[1]);
            
            parent.addChild(child);
        }
        
        // 그래프 순회
        List<Node> nearNodes = new ArrayList<>();
        nearNodes.add(nodes.get(0));
        dfs(nearNodes, 0, 0);
        
        return maxSheepNum;
    }
}