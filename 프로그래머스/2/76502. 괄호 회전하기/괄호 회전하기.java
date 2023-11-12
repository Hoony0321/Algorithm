import java.util.*;
class Solution {
    public boolean isValid(String s){
        Stack<String> stack = new Stack<>();
        
        for(String str : s.split("")){
            if(str.equals(")")){
                if(stack.isEmpty() || !stack.peek().equals("(")) return false;
                stack.pop();
                continue;
            }
            
            if(str.equals("]")){
                if(stack.isEmpty() || !stack.peek().equals("[")) return false;
                stack.pop();
                continue;
            }
            
            if(str.equals("}")){
                if(stack.isEmpty() || !stack.peek().equals("{")) return false;
                stack.pop();
                continue;
            }
            stack.add(str);
        }
        
        return stack.isEmpty() ? true : false;
    }
    
    public int solution(String s) {
        int answer = 0;
        
        for(int i = 0; i < s.length(); i++){
            String str = s.substring(i,s.length()) + s.substring(0,i);
            if(isValid(str)) answer++;
        }
        
        return answer;
    }
}