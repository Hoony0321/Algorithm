import java.util.*;

class Solution {
    public int solution(int sticker[]) {
        if(sticker.length == 1) return sticker[0];
        if(sticker.length == 2) return Math.max(sticker[0], sticker[1]);
        
        int[] sticker1 = new int[sticker.length];
        System.arraycopy(sticker,0,sticker1,0,sticker.length);
        sticker1[sticker1.length-1] = 0;
        int[] sticker2 = new int[sticker.length];
        System.arraycopy(sticker,0,sticker2,0,sticker.length);
        sticker2[0] = 0;
        
        int[] dp1 = new int[sticker1.length]; 
        int[] dp2 = new int[sticker2.length];
        dp1[0] = sticker1[0]; dp1[1] = Math.max(dp1[0], sticker1[1]);
        dp2[0] = sticker2[0]; dp2[1] = Math.max(dp2[0], sticker2[1]);
        
        for(int i = 2; i < sticker.length; i++){
            dp1[i] = Math.max(dp1[i-2] + sticker1[i], dp1[i-1]);
            dp2[i] = Math.max(dp2[i-2] + sticker2[i], dp2[i-1]);
        }
        
        int max = 0;
        for(int i = 0; i < 2; i++){
            max = Math.max(max, dp1[sticker.length-1-i]);
            max = Math.max(max, dp2[sticker.length-1-i]);
        }
        
        return max;
    }
}