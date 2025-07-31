import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Deque<Character> stack = new ArrayDeque<>();
        
        for(int i = 0; i < s.length(); i++){
            if(!stack.isEmpty() && stack.peekLast() == '(' && s.charAt(i) == ')'){
                stack.removeLast();  
                continue;
            }
            
            stack.addLast(s.charAt(i));
        }
        
        return stack.isEmpty();
    }
}