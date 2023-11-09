class Solution {
    class SkillInfo{
        public int type;
        public int y1;
        public int x1;
        public int y2;
        public int x2;
        public int degree;
        
        public SkillInfo(int[] data){
            this.type = data[0];
            this.y1 = data[1];
            this.x1 = data[2];
            this.y2 = data[3];
            this.x2 = data[4];
            this.degree = data[5];
        }
    }
    
    public int solution(int[][] board, int[][] skill) {
        int answer = 0;
        int[][] sumBoard = new int[board.length+1][board[0].length+1];
        
        for(int[] elem : skill){
            SkillInfo skillInfo = new SkillInfo(elem);
            
            // 왼쪽 상단
            sumBoard[skillInfo.y1][skillInfo.x1] += 
                    skillInfo.type == 1 ? -skillInfo.degree : skillInfo.degree;
            
            // 오른쪽 하단
            sumBoard[skillInfo.y2+1][skillInfo.x2+1] += 
                    skillInfo.type == 1 ? -skillInfo.degree : skillInfo.degree;
            
            // 오른쪽 상단
            sumBoard[skillInfo.y1][skillInfo.x2+1] +=
                    skillInfo.type == 1 ? skillInfo.degree : -skillInfo.degree;
            
            // 왼쪽 하단
            sumBoard[skillInfo.y2+1][skillInfo.x1] += 
                    skillInfo.type == 1 ? skillInfo.degree : -skillInfo.degree;
        }
        
        // 누적합
        // 행 진행
        for(int i = 0; i < sumBoard[0].length-1; i++){
            for(int j = 0; j < sumBoard.length; j++){
                sumBoard[j][i+1] += sumBoard[j][i];
            }
        }
        
        // 열 진행
        for(int i = 0; i < sumBoard.length-1; i++){
            for(int j = 0; j < sumBoard[0].length; j++){
                sumBoard[i+1][j] += sumBoard[i][j];
            }
        }
        
        
        // 결과
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(board[i][j] + sumBoard[i][j] > 0) answer++;
            }
        }
        
        return answer;
    }
}