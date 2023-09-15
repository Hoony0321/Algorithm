import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        long max_action = 2 * (queue1.length + queue2.length);
        Queue<Integer> q1 = new LinkedList<Integer>();
        Queue<Integer> q2 = new LinkedList<Integer>();
        long sum1 = 0;
        long sum2 = 0;
        long target = 0;
        
        for(int e : queue1){
            q1.add(e);
            sum1 += e;
        }
        for(int e : queue2){
            q2.add(e);
            sum2 += e;
        }
        if((sum1 + sum2) % 2 != 0) return -1; // 두 큐의 합을 같게 만들 수 없음.
        target = (long) (sum1 + sum2) / 2;
        
        while(sum1 != sum2 && answer <= max_action){
            if(sum1 > sum2){
                int elem = q1.poll();
                q2.add(elem);
                sum1 -= elem;
                sum2 += elem;
            }else {
                int elem = q2.poll();
                q1.add(elem);
                sum2 -= elem;
                sum1 += elem;
            }
            
            answer++;
        }
        
        return answer > max_action ? -1 : answer;
    }
}