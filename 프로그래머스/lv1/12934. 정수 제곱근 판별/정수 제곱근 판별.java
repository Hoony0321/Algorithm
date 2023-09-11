class Solution {
    public long solution(long n) {
        long answer = 0;
        
        double sqrtN = Math.sqrt(n);
        
        if(sqrtN == (double)((int)sqrtN)){
            return (long) Math.pow((int) (sqrtN+1), 2);
        }
        
        return -1;
    }
}