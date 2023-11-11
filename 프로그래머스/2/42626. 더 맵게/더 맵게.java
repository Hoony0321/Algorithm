import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> heapq = new PriorityQueue<>();
        
        for(int scov : scoville){
            heapq.add(scov);
        }
        
        while(heapq.peek() < K && heapq.size() > 1){
            int scov1 = heapq.poll();
            int scov2 = heapq.poll();
            int newScov = scov1 + scov2 * 2;
            
            heapq.add(newScov);
            answer++;
        }
        
        return heapq.peek() < K ? -1 : answer;
    }
}