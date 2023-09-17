import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Deque<Integer> deque = new LinkedList<Integer>();
        
        for(int num : arr){
            if(!deque.isEmpty() && deque.peekLast() == num) continue;
            deque.addLast(num);
        }
        
        int[] answer = new int[deque.size()];
        int index = 0;
        while(!deque.isEmpty()){
            answer[index++] = deque.pollFirst();
        }

        return answer;
    }
}