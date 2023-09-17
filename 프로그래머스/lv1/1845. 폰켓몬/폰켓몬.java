import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        int numChoice = nums.length / 2;
        Set<Integer> numType = new HashSet<>();
        
        for(int num : nums){
            numType.add(num);
        }
        
        return numChoice >= numType.size() ? numType.size() : numChoice;
    }
}