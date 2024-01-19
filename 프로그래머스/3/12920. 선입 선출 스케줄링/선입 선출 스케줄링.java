import java.util.*;

class Solution {
    
    public long getTotalJob(int[] cores, long mid){
        long totalJob = 0;
        for(int core : cores){
            totalJob += mid / core;
        }
        
        return totalJob;
    }
    
    public int solution(int n, int[] cores) {
        
        n -= cores.length;
        long low = 1;
        long high = 10000 * 50000;
        
        while(low < high){
            long mid = (low + high)/2;
            long totalJob = getTotalJob(cores, mid);
            if(totalJob >= n){
                high = mid;
                continue;
            }
            
            low = mid+1;
        }
        
        long remain = n - getTotalJob(cores, high-1);
        for(int i = 0; i < cores.length; i++){
            if(high % cores[i] == 0){
                remain--;
                if(remain <= 0) return i+1;
            }
        }

        
        return 0;
    }
}