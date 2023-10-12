class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        int maxRange = 2 * w + 1;
        
        int prev = 1;
        for(int station : stations){
            
            int start = station - w;
            int end = station + w;
            
            if(prev < start){ // 새로운 기지국 설치 필요
                int num = start - prev;
                answer += num / maxRange;
                if(num % maxRange != 0){
                    answer += 1;
                }
            }
            
            prev = end+1;
        }
        
        if(prev <= n){
            int num = n - prev + 1;
            answer += num / maxRange;
            if(num % maxRange != 0) answer += 1;
        }
        

        return answer;
    }
}