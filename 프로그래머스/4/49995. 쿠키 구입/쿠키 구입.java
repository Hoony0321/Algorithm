

class Solution {
    public int solution(int[] cookie) {
        int answer = 0;
        int n = cookie.length;
        int[] prefixSum = new int[n];
        
        // 누적합 계산
        prefixSum[0] = cookie[0];
        for(int i = 0; i < n-1; i++){
            prefixSum[i+1] = prefixSum[i] + cookie[i+1];
        }
        
        for(int mid = 0; mid < n-1; mid++){
            int left = mid;
            int right = mid+1;
            while(left >= 0 && right < n){
                int leftSum = left != 0 ? prefixSum[mid] - prefixSum[left-1] : prefixSum[mid];
                int rightSum = prefixSum[right] - prefixSum[mid];

                if(leftSum == rightSum){
                    answer = Math.max(answer, leftSum);
                    left -= 1;
                    right += 1;
                }
                else if(leftSum > rightSum){
                    right += 1;
                }
                else{
                    left -= 1;
                }   
            } 
        }
        
        return answer;
    }
}