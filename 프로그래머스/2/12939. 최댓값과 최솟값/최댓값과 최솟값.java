class Solution {
    public String solution(String s) {
        int maxNumber = Integer.MIN_VALUE;
        int minNumber = Integer.MAX_VALUE;
        for(String str : s.split(" ")){
            int number = -1;
            
            if(str.charAt(0) == '-'){ // 음수인 경우
                number = Integer.parseInt(str.substring(1));
                number *= -1;
            }
            
            if(str.charAt(0) != '-'){ // 양수인 경우
                number = Integer.parseInt(str);   
            }
             
            maxNumber = Math.max(maxNumber, number);
            minNumber = Math.min(minNumber, number);
        }
        
        String answer = String.format("%d %d", minNumber, maxNumber);
        return answer;
    }
}