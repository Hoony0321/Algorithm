class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {0,0};
        int yh = 0;
        
        while(true){
            yh++;
            int yw = yellow / yh;
            if(yellow % yh != 0) continue; // 나누어 떨어지지 않는 경우
            
            int needBrown = 2 * (yw + yh) + 4;
            
            if(needBrown == brown){
                answer[0] = yw+2;
                answer[1] = yh+2;
                break;
            }
        }
        
        
        return answer;
    }
}