import java.util.*;

class Solution {
    public long solution(long n) {
        
        String strNum = Long.toString(n);
        int[] numArr = new int[strNum.length()];
        
        for(int i = 0; i < strNum.length(); i++){
            numArr[i] = Integer.valueOf(strNum.charAt(i) - '0');
        }
        Arrays.sort(numArr);
        
        long answer = 0;
        for(int i = 0; i < numArr.length; i++){
            answer += numArr[i] * Math.pow(10, i);
        }
        
        
        return answer;
    }
}