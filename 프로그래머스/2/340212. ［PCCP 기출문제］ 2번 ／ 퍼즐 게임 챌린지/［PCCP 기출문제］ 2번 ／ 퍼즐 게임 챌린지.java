import java.util.*;

class Solution {
    public boolean checkIsPossible(int[] diffs, int[] times, long limit, int level){
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

    public int binarySearch(int[] diffs, int[] times, long limit){
        int left = 1;
        int right = Arrays.stream(diffs).max().getAsInt();
        int minimum = right;
        while(left <= right){
            int mid = (left + right) / 2;
            if(checkIsPossible(diffs, times, limit, mid)){
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
        return binarySearch(diffs, times, limit);
        
    }
}