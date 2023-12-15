class Solution {
    
    private String convertToBinary(long number){
        String binary = "";
        
        while(number > 0){
            long remainder = number % 2;
            number /= 2;
            binary = Long.toString(remainder) + binary;
        }
        
        return binary;
    }
    
    private Boolean judgeBinaryTree(String binaryTree, boolean isZero){
        // System.out.println(String.format("isZero : %b", isZero));
        if(binaryTree.length() % 2 == 0){ // 개수가 짝수이면 
            return false;
        }
        if(isZero){
            boolean isAvailable = true;
            for(int i = 0; i < binaryTree.length(); i++){
                if(binaryTree.charAt(i) == '1'){
                    isAvailable = false;
                    break;
                }
            }
            
            // System.out.println(String.format("isAvailable : %b", isAvailable));
            return isAvailable;
        }
        
        if(binaryTree.length() == 1) return true;
        
        int midIdx = binaryTree.length() / 2;
        boolean nextIsZero = binaryTree.charAt(midIdx) == '0';
        
        return judgeBinaryTree(binaryTree.substring(0,midIdx), nextIsZero) && 
            judgeBinaryTree(binaryTree.substring(midIdx+1,binaryTree.length()), nextIsZero);
    }
    
    public int[] solution(long[] numbers) {
        int[] answer = new int[numbers.length];
        
        for(int i = 0; i < numbers.length; i++){
            long number = numbers[i];
            
            // convert to binary
            String binary = convertToBinary(number);
            // System.out.println(String.format("binary : %s", binary));
            
            
            // judge binary tree
            int midIdx = binary.length() / 2;
            boolean result = false;
            for(int j = 0; j <= midIdx; j++){
                if(j > (binary.length() - j - 1)) continue; // 왼쪽이 오른쪽보다 많으면 불가능.
                if(binary.charAt(j) != '1') continue; // 뿌리노드가 0일순 없음.
                
                String binaryTree = new String(binary);
                for(int k = 0; k < (binary.length() - j - 1) - j; k++){
                    binaryTree = "0" + binaryTree;
                }
                
                result = judgeBinaryTree(binaryTree,false);
                // System.out.println(String.format("tree : %s | mid : %d | result : %b", binaryTree, j, result));
                if(result) break;
            }
            
            answer[i] = result ? 1 : 0;
        }
        
        
        return answer;
    }
}