import java.util.*;

class Solution {
    private int[] diffs;
    private int[] times;
    private long limit;
    
    public boolean checkIsPossible(int level){
        long requireTime = 0;
        int n = diffs.length;
        for(int i = 0; i < n; i++){
            if(diffs[i] <= level){
                requireTime += times[i];
            }
            else if(diffs[i] > level){
                requireTime += (diffs[i] - level) * (times[i-1] + times[i]) + times[i];
            }
        }

        return requireTime <= limit ? true : false;
    }

    public int binarySearch(){
        int left = 1;
        int right = Arrays.stream(diffs).max().getAsInt();
        int minimum = right;
        while(left <= right){
            int mid = (left + right) / 2;
            if(checkIsPossible(mid)){
                minimum = Math.min(right,mid);
                right = mid-1;
            }
            else{
                left = mid+1;
            }   
        }
        
        return minimum;
    }
    
    public int solution(int[] diffs, int[] times, long limit) {
        this.diffs = diffs;
        this.times = times;
        this.limit = limit;
        return binarySearch();
        
    }
}