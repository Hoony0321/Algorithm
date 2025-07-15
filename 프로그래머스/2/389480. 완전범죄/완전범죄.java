import java.util.*;

class Solution {
    public int solution(int[][] info, int n, int m) {
        int MAX_VALUE = 3 * 40 + 1;
        int answer = MAX_VALUE;
        
        // dp 선언
        int[][] dp = new int[info.length][3*40+1];
        for(int i = 0; i < info.length; i++){
            for(int j = 0; j < 3*40+1; j++){
                dp[i][j] = MAX_VALUE;
            }
        }
        
        // deque 선언
        Deque<int[]> deque = new ArrayDeque<>();
        deque.addFirst(new int[]{0,info[0][0],0});
        deque.addFirst(new int[]{0,0,info[0][1]});
        
        // main 함수
        while(!deque.isEmpty()){
            int[] elem = deque.removeLast();
            int i = elem[0];
            int traceSumA = elem[1];
            int traceSumB = elem[2];
            
            if(traceSumA >= n) continue;
            if(traceSumB >= m) continue;
            if(dp[i][traceSumB] <= traceSumA) continue;
            dp[i][traceSumB] = traceSumA;
            
            if(i == info.length-1) continue;
            deque.addFirst(new int[]{i+1,traceSumA + info[i+1][0], traceSumB});
            deque.addFirst(new int[]{i+1,traceSumA, traceSumB + info[i+1][1]});
        }
        
        for(int i = 0; i < m+1; i++){
            if(dp[info.length-1][i] < answer){
                answer = dp[info.length-1][i];
            }
        }
        
        if(answer == MAX_VALUE){
            return -1;
        }
        
        return answer;
    }
}