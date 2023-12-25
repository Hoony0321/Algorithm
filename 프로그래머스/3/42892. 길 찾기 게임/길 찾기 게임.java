import java.util.*;

class Solution {
    
    public int[] convertListToArray(List<Integer> list){
        int[] result = new int[list.size()];
        for(int i = 0; i < list.size(); i++){
            result[i] = list.get(i);
        }
        
        return result;
    }
    
    public Node findRootNode(List<int[]> nodeinfoList, int start, int end){
        if(start == end){ // leaf node인 경우
            return new Node(nodeinfoList.get(start)[2]);
        }
        if(start > end){ // 범위를 벗어난 경우
            return null;
        }
        
        // root index 찾기
        int rootIdx = start;
        for(int i = start+1; i <= end; i++){
            if(nodeinfoList.get(i)[1] > nodeinfoList.get(rootIdx)[1]) rootIdx = i;
        }
        
        // node 생성
        Node rootNode = new Node(nodeinfoList.get(rootIdx)[2]);
        Node leftChildNode = findRootNode(nodeinfoList, start, rootIdx-1);
        Node rightChildNode = findRootNode(nodeinfoList, rootIdx+1, end);
        
        // child node 연결
        rootNode.setLeft(leftChildNode);
        rootNode.setRight(rightChildNode);
        
        return rootNode;
    }
    
    public void preorder(Node node, List<Integer> result){
        result.add(node.number);
        if(node.left != null) preorder(node.left, result);
        if(node.right != null) preorder(node.right, result);
    }
    
    public void postorder(Node node, List<Integer> result){
        if(node.left != null) postorder(node.left, result);
        if(node.right != null) postorder(node.right, result);
        result.add(node.number);
    }
    
    public int[][] solution(int[][] nodeinfo) {
        // nodeinfoList 생성
        List<int[]> nodeinfoList = new ArrayList<>();
        for(int i = 0; i < nodeinfo.length; i++){
            // x, y, 노드 번호 순으로 새롭게 저장
            nodeinfoList.add(new int[]{nodeinfo[i][0], nodeinfo[i][1], i+1}); 
        }
        
        // nodeinfoList 정렬 (x 값 기준으로 오름차순)
        Collections.sort(nodeinfoList, (o1,o2) -> o1[0] - o2[0]);
        
        
        // root node 찾기
        Node treeRootNode = findRootNode(nodeinfoList, 0, nodeinfoList.size()-1);
        
        // 전위 순회
        List<Integer> preorderResult = new ArrayList<>();
        preorder(treeRootNode, preorderResult);
        
        // 후위 순회
        List<Integer> postorderResult = new ArrayList<>();
        postorder(treeRootNode, postorderResult);
        
        int[][] answer = {convertListToArray(preorderResult), convertListToArray(postorderResult)};
        return answer;
    }
    
    class Node {
        int number;
        Node left;
        Node right;
        
        public Node(int number){
            this.number = number;
            left = null;
            right = null;
        }
        
        public void setLeft(Node node){
            left = node;
        }
        
        public void setRight(Node node){
            right = node;
        }
    }
}