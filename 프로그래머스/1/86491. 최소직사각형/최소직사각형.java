import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        
        int maxSize = 0;
        int minSize = 0;
        
        for(int[] size : sizes){
            maxSize = Math.max(maxSize, Math.max(size[0], size[1]));
            minSize = Math.max(minSize, Math.min(size[0], size[1]));
        }

        return maxSize * minSize;
    }
}