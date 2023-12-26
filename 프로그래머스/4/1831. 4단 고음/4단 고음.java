class Solution {
	// 몇 번의 곱셈이 필요한지 계산.
    public int getRemainMul(int n){
        return (int)(Math.log(n) / Math.log(3));
    }
    
    // 재귀적으로 수행하며 계산
    public int getSimulation(int n , int numMul, int numPlus){
    	// 종료 조건 정의
        if(numMul*2 < numPlus)
            return 0;
        if(n == 3 && numMul == 1 && numPlus == 0)
            return 1;
        if(n == 4 && numMul == 1 && numPlus == 1)
            return 1;
        if(n == 5 && numMul == 1 && numPlus == 2)
            return 1;
        
        // 재귀 수행 정의
        int count = 0;
        for(int i = 0; i <= numPlus; ++i){
            if((n-i > 0) && (n-i) % 3 == 0){
                count += getSimulation((n - i) /3, numMul - 1, numPlus - i);
            }
        }
        
        return count;
    }
    
    public int solution(int n) {
        int numMul = getRemainMul(n);
        int numPlus = numMul * 2;
        
        int result = getSimulation(n - 2, numMul, numPlus - 2);
        return result;
    }
}