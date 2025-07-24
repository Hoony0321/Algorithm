import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int choiceNum = nums.length / 2;
        Set<Integer> numSet = new HashSet<>();
        for(int num : nums) numSet.add(num);
        
        return numSet.size() <= choiceNum ? numSet.size() : choiceNum;
    }
}