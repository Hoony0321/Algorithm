import java.util.*;

class Solution {
    List<Node> nodes = new ArrayList<>();
    boolean canDivide = true;
    int divideCount = 0;
    Node root;
    
    public boolean search(int maxPeople, int k){
        canDivide = true;
        divideCount = 0;
        splitGroup(root, maxPeople);
        if(!canDivide) return false;
        if(divideCount >= k) return false;
        return true;
    }
    
    public int splitGroup(Node node, int maxPeople){
        if(node == null) return 0;
        if(node.examinee > maxPeople){
            canDivide = false;
            return -1;
        }
        
        int CUR = node.examinee;
        int LC = splitGroup(node.left, maxPeople);
        int RC = splitGroup(node.right, maxPeople);
        if(!canDivide) return 0;
        
        if(CUR + LC + RC <= maxPeople) return CUR + LC + RC;
        
        if(CUR + LC > maxPeople && CUR + RC > maxPeople){
            divideCount += 2;
            return CUR;
        }
        
        if(CUR + LC > maxPeople){
            divideCount += 1;
            return CUR + RC;
        }
        
        if(CUR + RC > maxPeople){
            divideCount += 1;
            return CUR + LC;
        }
        
        if(CUR + RC <= maxPeople && CUR + LC <= maxPeople){
            divideCount += 1;
            return CUR + Math.min(LC, RC);
        }
        
        System.out.println("error");
        return Integer.MIN_VALUE;
    }
    
    public int solution(int k, int[] num, int[][] links) {
        setBinaryTree(num, links);
        
        int answer = Integer.MAX_VALUE;
        int low = 1;
        int high = 10000 * 10000;
        while(low <= high){
            int mid = (low + high) / 2;
            if(search(mid, k)){
                answer = Math.min(answer, mid);
                high = mid-1;
            }
            else{
                low = mid+1;
            }
        }
        
        return answer;
    }
    
    public void setBinaryTree(int[] num, int[][] links){
        for(int i = 0; i < num.length; i++){
            nodes.add(new Node(i));
        }
        for(int i = 0; i < links.length; i++){
            Node node = nodes.get(i);
            
            if(links[i][0] != -1){
                node.setLeft(nodes.get(links[i][0]));
            }
            
            if(links[i][1] != -1){
                node.setRight(nodes.get(links[i][1]));
            }
            
            node.setExaminee(num[i]);
        }
        
        for(Node node : nodes){
            if(node.parent == null){
                root = node;
                break;
            }
        }
    }
    
    class Node {
        int id;
        int examinee;
        Node left;
        Node right;
        Node parent;
        
        public Node(int id){
            this.id = id;
            this.examinee = 0;
            this.parent = null;
            this.left = null;
            this.right = null;
        }
        
        public void setLeft(Node node){
            node.parent = this;
            this.left = node;
        }
        
        public void setRight(Node node){
            node.parent = this;
            this.right = node;
        }
        
        public void setExaminee(int examinee){
            this.examinee = examinee;
        }
    }
}