class Solution {
    
    public boolean isPrime(int num){
        int divide = 2;
        while(divide <= num / 2){
            if(num % divide == 0) return false;
            divide++;
        }
        
        return true;
    }
    
    public int solution(int[] nums) {
        int answer = 0;

        for(int i = 0; i < nums.length-2; i++){
            for(int j = i+1; j < nums.length-1; j++){
                for(int k = j+1; k < nums.length; k++){
                    if(isPrime(nums[i] + nums[j] + nums[k])) answer += 1;
                }
            }
        }

        return answer;
    }
}