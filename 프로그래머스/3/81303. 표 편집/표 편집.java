import java.util.*;

class Node{
        Node prev = null;
        Node next = null;
        int value = -1;
        
        Node(int value){
            this.value = value;
        }
    
        public void setPrev(Node prev){
            this.prev = prev;
        }
    
        public void setNext(Node next){
            this.next = next;
        }
    
        public void remove(){
            Node prevNode = this.prev;
            Node nextNode = this.next;
            
            if(nextNode != null) nextNode.prev = prevNode;
            if(prevNode != null) prevNode.next = nextNode;
        }
    }

class Solution {
    Node[] nodes;
    Stack<Node> cash = new Stack<Node>();
    Node pointer;
    
    
    public void execCmd(String cmd){
        String[] cmds = cmd.split(" ");
        if(cmds[0].equals("D")){
            int num = Integer.parseInt(cmds[1]);
            while(num > 0){
                pointer = pointer.next;
                num--;
            }
        }
        else if(cmds[0].equals("U")){
            int num = Integer.parseInt(cmds[1]);
            while(num > 0){
                pointer = pointer.prev;
                num--;
            }
        }
        else if(cmds[0].equals("C")){
            Node nextPointer = pointer.next == null ? pointer.prev : pointer.next;
            
            // 원소 삭제 -> 링크 변경
            pointer.remove();
            
            // 캐시 추가
            cash.push(pointer);
            
            // 포인터 변경
            pointer = nextPointer;
        }
        else if(cmds[0].equals("Z")){
            Node insertNode = cash.pop();
            
            // 변경 노드 세팅
            Node prevNode = insertNode.prev;
            Node nextNode = insertNode.next;
            
            // 링크 변경
            if(prevNode != null) prevNode.next = insertNode;
            if(nextNode != null) nextNode.prev = insertNode;
        }
    }
    
    public String solution(int n, int k, String[] cmd) {
        // 시작 데이터 세팅
        nodes = new Node[n];
        for(int i = 0; i < n; i++){
            nodes[i] = new Node(i);
        }
        
        // 노드 연결 진행
        for(int i = 0; i < n; i++){
            if(i == 0){
                nodes[i].setNext(nodes[i+1]);
            }
            else if(i == n-1){
                nodes[i].setPrev(nodes[i-1]);
            }
            else{
                nodes[i].setNext(nodes[i+1]);
                nodes[i].setPrev(nodes[i-1]);
            }
        }
        
        // pointer 시작 위치로 이동
        pointer = nodes[k];
        
        // 명령 실행
        for(String cmdElem : cmd){
            execCmd(cmdElem);
        }
        
        String[] answer = new String[n];
        Arrays.fill(answer,"O");
        while(!cash.isEmpty()){
            Node node = cash.pop();
            answer[node.value] = "X";
        }
        
        return String.join("", answer);

    }
}