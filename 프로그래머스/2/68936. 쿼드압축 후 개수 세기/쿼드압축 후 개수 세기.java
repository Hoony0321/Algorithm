class Solution {
    int[] answer = new int[2];
    
    private void compressArray(int[][] arr){
        int size = arr.length;
        int targetNum = arr[0][0];
        boolean canCompress = true;
        
        for(int i = 0; i < size; i++){
            if(!canCompress) break;
            for(int j = 0; j < size; j++){
                if(arr[i][j] != targetNum){
                    canCompress = false;
                    break;
                }
            }
        }
        
        if(canCompress){ // 탈출 조건
            answer[targetNum] += 1;
            return;
        }
        
        // 4개의 영역으로 나눈 뒤 다시 실행
        int splitedSize = size / 2;
        int[][] dxy = new int[][]{{0,0}, {1,0}, {0,1}, {1,1}};
        
        for(int i = 0; i < 4; i++){
            int[][] splitedArray = new int[splitedSize][splitedSize];
            int y = dxy[i][0] * splitedSize;
            int x = dxy[i][1] * splitedSize;
            
            for(int p = 0; p < splitedSize; p++){
                for(int q = 0; q < splitedSize; q++){
                    splitedArray[p][q] = arr[y + p][x + q];
                }
            }
            
            compressArray(splitedArray);
        }
        
        
    }
    
    public int[] solution(int[][] arr) {
        compressArray(arr);
        
        return answer;
    }
}