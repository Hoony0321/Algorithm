import java.util.*;
class Solution {
    public int solution(int[] a) {
        int answer = 0;
        int n = a.length;
        int leftMin = 1000000001;
        int rightMin = 1000000001;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        Map<Integer,Boolean> checkMap = new HashMap<>();
        
        // 양쪽 끝은 무조건 가능
        answer += 2;
        
        // left/right min 설정
        leftMin = a[0];
        for(int i = 2; i < n; i++){
            pq.add(a[i]);
            checkMap.put(a[i], true);
        }
        rightMin = pq.poll();
        
        for(int i = 1; i < n-1; i++){
            checkMap.put(a[i], false);
            
            // left/right min 설정
            leftMin = Math.min(leftMin, a[i-1]);
            while(!checkMap.get(rightMin)){
                rightMin = pq.poll();
            }
            
            if(leftMin > a[i] || rightMin > a[i]) answer += 1;
            
            
        }
        
        return answer;
    }
}