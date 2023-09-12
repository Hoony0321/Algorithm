import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;

class Solution {
    public String solution(String number, int k) {
        String answer = "";
        Stack<Character> stack = new Stack<>();
        
        for(char c : number.toCharArray()) {
            while(!stack.empty() && stack.peek() < c && k > 0){
                stack.pop();
                k -= 1;
            }
            
            stack.push(c);
        }
        
        while(k > 0){
            stack.pop();
            k -= 1;
        }
        
        for(char c : stack){
            answer += c;
        }
        
        return answer;
    }
}