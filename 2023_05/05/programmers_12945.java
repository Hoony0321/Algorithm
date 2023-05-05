//문제설명
//programmers_12945 - 피보나치 수 (난이도 2)

class Solution {
    public int solution(int n) {
        int[] dp = new int[100001];
        dp[0] = 0; dp[1] = 1;
        
        for(int i = 2; i < n+1; i++){
            dp[i] = (dp[i-1] + dp[i-2]) % 1234567;
        }
        
        return dp[n];
    }
}