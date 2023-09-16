import java.util.*;

class Solution {
    public int countNumberOne (int n){
        int numberOfOne = 0;
        while(n > 0){
            numberOfOne += n % 2 == 1 ? 1 : 0;
            n /= 2;
        }
        
        return numberOfOne;
    }
    public int solution(int n) {
        int targetNumberOfOne = countNumberOne(n);
        
        while(true){
            int numberOfOne = countNumberOne(++n);
            
            if(targetNumberOfOne == numberOfOne) return n;
        }
    }
}