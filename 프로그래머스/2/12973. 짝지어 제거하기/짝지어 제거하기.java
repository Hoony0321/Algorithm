import java.util.*;

class Solution
{
    public int solution(String s)
    {
        Stack<Character> stack = new Stack<>();
        
        for(int i = 0; i < s.length(); i++){
            if(!stack.isEmpty()){
                if(stack.peek() == s.charAt(i)){
                    stack.pop();
                    continue;
                }
            }
            
            stack.add(s.charAt(i));
        }

        return stack.isEmpty() ? 1 : 0;
    }
}