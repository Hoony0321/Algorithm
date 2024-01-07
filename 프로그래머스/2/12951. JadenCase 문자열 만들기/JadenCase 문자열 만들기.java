class Solution {
    
    public String solution(String s) {
        String answer = "";
        s = s.toLowerCase();
        for(int i = 0; i < s.length(); i++){
            if(i == 0 || s.charAt(i-1) == ' '){
                answer += s.substring(i,i+1).toUpperCase();
                continue;
            }
            
            answer += s.substring(i,i+1);
        }
        
        return answer;
    }
}