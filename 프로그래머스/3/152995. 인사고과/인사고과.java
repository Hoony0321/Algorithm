class Solution {
    public int solution(int[][] scores) {
        int answer = 1;

        for(int i = 1; i < scores.length; i++){
            if(scores[i][0] + scores[i][1] <= scores[0][0] + scores[0][1]) continue;
            if(scores[i][0] > scores[0][0] && scores[i][1] > scores[0][1]) return -1;
            
            boolean check = false;
            for(int j = 1; j < scores.length; j++){
                if(scores[i][0] < scores[j][0] && scores[i][1] < scores[j][1]){
                    check = true;
                    break;
                }
            }
            
            if(!check) answer++;
            
        }
        
        return answer;
    }
}