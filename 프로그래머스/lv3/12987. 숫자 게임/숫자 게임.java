import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        
        Arrays.sort(A);
        Arrays.sort(B);
        
        Deque<Integer> deque = new ArrayDeque<>();
        for(int num : B){
            deque.add(num);
        }
        
        for(int i = A.length-1; i >= 0; i--){
            if(deque.peekLast() > A[i]){
                deque.pollLast();
                answer += 1;
            } else {
                deque.pollFirst();
            }
        }
        
        
        return answer;
    }
}