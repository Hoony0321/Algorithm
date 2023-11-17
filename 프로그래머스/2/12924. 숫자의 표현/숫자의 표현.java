class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for(int start = 1; start <= n; start++){
            int current = start;
            int remain = n;
            while(remain > 0){
                remain -= current;
                current++;
            }
            
            if(remain == 0) answer++;
        }
        
        return answer;
    }
}