import java.util.*;

class Solution {
    int totalInputCount = 0;
    
    public void setTree(Node root, String word){
        Node curNode = root;
        for(int i = 0; i < word.length(); i++){
            char alphabet = word.charAt(i);
            curNode.addChild(alphabet);
            curNode = curNode.children.get(alphabet);
        }
    }
    
    public void findInputCount(Node root, String word){
        Node curNode = root;
        for(int i = 0; i < word.length(); i++){
            char alphabet = word.charAt(i);
            curNode = curNode.children.get(alphabet);
            totalInputCount++;
            
            if(curNode.count == 1) break;
        }
    }
    
    public int solution(String[] words) {
        Node root = new Node(' ');
        
        // Tree 구축
        for(String word : words){
            setTree(root, word);
        }
        
        // 입력해야 되는 문자 개수 찾기
        for(String word : words){
            findInputCount(root, word);
        }
        
        return totalInputCount;
    }
    
    class Node {
        Integer count;
        Character alphabet;
        Map<Character, Node> children = new HashMap<>();
        
        public Node(char alphabet){
            this.count = 0;
            this.alphabet = alphabet;
        }
        
        public void addChild(char alphabet){
            if(!children.containsKey(alphabet)){ // 해당 child가 존재하지 않는 경우
                Node child = new Node(alphabet);
                children.put(alphabet, child);
            }
            
            children.get(alphabet).count++;
        }
    }
}