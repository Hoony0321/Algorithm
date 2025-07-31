import java.util.*;
class Process {
    int id;
    int priority;
    
    public Process(int id, int priority){
        this.id = id;
        this.priority = priority;
    }
}

class Solution {
    public int solution(int[] priorities, int location) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> b - a);
        Deque<Process> q = new ArrayDeque<>();
        
        for(int i = 0; i < priorities.length; i++){
            pq.add(priorities[i]);
            q.addLast(new Process(i, priorities[i]));
        }
        
        int answer = 0;
        while(true){
            Process pr = q.removeFirst();
            if(pr.priority == pq.peek()){
                pq.poll();
                answer += 1;                
                if(pr.id == location) break;
            }
            else{
                q.addLast(pr);
            }
        }
        
        return answer;
    }
}