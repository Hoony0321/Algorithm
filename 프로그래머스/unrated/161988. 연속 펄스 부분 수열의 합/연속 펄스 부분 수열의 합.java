import java.util.*;

class Solution {
    
    
    public long solution(int[] sequence) {
        long answer = 0;    
        long blankNum = -100001;
        long[] dp1 = new long[]{};
        long[] dp2 = new long[]{};
        
        dp1 = new long[sequence.length];
        dp2 = new long[sequence.length];
        Arrays.fill(dp1,blankNum);
        Arrays.fill(dp2,blankNum);
        
        Stack<Integer> stack1 = new Stack<>();
        Stack<Integer> stack2 = new Stack<>();
        
        stack1.add(0);
        stack2.add(0);
        
        while(!stack1.isEmpty()){
            int n = stack1.pop();
            
            if(dp1[n] != blankNum) continue;
            
            if(n == 0){
                dp1[0] = sequence[0] * 1;
            }
            else{
                dp1[n] = dp1[n-1] > 0 ? dp1[n-1] + sequence[n] * (long) Math.pow(-1,n) : sequence[n] * (long) Math.pow(-1,n);    
            }
            
            
            if(dp1[n] > answer) answer = dp1[n];
            if(n == sequence.length-1) continue;
            stack1.add(n+1);
        }
        
        while(!stack2.isEmpty()){
            int n = stack2.pop();
            
            if(dp2[n] != blankNum) continue;
            if(n == 0){
                dp2[0] = sequence[0] * -1;
            }
            else {
                dp2[n] = dp2[n-1] > 0 ? dp2[n-1] + sequence[n] * (long) Math.pow(-1,n+1) : sequence[n] * (long) Math.pow(-1,n+1);    
            }
            
            
            if(dp2[n] > answer) answer = dp2[n];
            if(n == sequence.length-1) continue;
            stack2.add(n+1);
        }
        
        // for(long num : dp1){
        //     System.out.print(num);
        //     System.out.print(" ");
        // }
        
        return answer;
    }
}