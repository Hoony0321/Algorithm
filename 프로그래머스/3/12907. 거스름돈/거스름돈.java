class Solution {
    public int solution(int n, int[] money) {
        int[] dp = new int[n+1];
        dp[0] = 1;
        
        for(int elem : money){
            for(int i = elem; i <= n; i++){
                dp[i] += dp[i - elem];
            }
        }
        
        return dp[n];
    }
}