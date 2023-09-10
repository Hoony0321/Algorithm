class Solution {
    public int[] solution(long n) {
        String nString = Long.toString(n);
        int[] answer = new int[nString.length()];
            
        for(int i = 0; i < nString.length(); i++){
            answer[i] = Character.getNumericValue(nString.charAt(nString.length()-1 - i));
        }    
        
        return answer;
    }
}