import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        Deque<Integer> stack = new ArrayDeque<>();
        
        for(int i = 0; i < prices.length; i++){
            while(!stack.isEmpty() && prices[i] < prices[stack.peekFirst()]){
                int elemIdx = stack.pollFirst();
                answer[elemIdx] = i - elemIdx;
            }
            
            stack.addFirst(i);
        }
        
        for(int i : stack){
            answer[i] = prices.length-1 - i;
        }
        
        return answer;
    }
}