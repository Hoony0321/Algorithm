import java.util.Stack;
import java.util.List;
import java.util.ArrayList;

class Solution {
    public int solution(int[] order) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();
        
        int orderIdx = 0;
        
        for(int box = 1; box <= order.length; box++){
            if(order[orderIdx] == box){ // 같은 경우
                answer++;
                orderIdx++;
            }
            else{ // 다른 경우
                stack.push(box);
            }
            
            while(!stack.isEmpty() && order[orderIdx] == stack.peek()){
                answer++;
                stack.pop();
                orderIdx++;
            }
            
            
        }
        
        
        return answer;
    }
}