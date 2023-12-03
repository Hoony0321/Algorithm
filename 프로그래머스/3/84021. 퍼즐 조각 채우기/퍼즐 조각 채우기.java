import java.util.*;

class Solution {
    int[][] dxys = {{1,0}, {-1,0}, {0,1}, {0,-1}};
    
    class SectionRectangle {
        int size = 0;
        int w = 0;
        int h = 0;
        int[][] rectangle;
        
        public SectionRectangle(List<int[]> section){
            // rectangle 초기화
            int[] rectangeSize = findRectangleSize(section);
            int h = rectangeSize[0];
            int w = rectangeSize[1];
            int minY = rectangeSize[2];
            int minX = rectangeSize[3];
            
            this.w = w;
            this.h = h;
            
            rectangle = new int[h][w];
            for(int i = 0; i < h; i++){
                for(int j = 0; j < w; j++){
                    rectangle[i][j] = 0;
                }
            }
            
            // rectangle 설정
            int sectionSize = 0;
            for(int i = 0; i < section.size(); i++){
                int y = section.get(i)[0];
                int x = section.get(i)[1];
                rectangle[y - minY][x - minX] = 1;
                sectionSize++;
            }
            
            // section size 설정
            this.size = sectionSize;
        }
        
        public void rotate(){
            int[][] rotatedRectangle = new int[rectangle[0].length][rectangle.length];
            
            for(int i = 0; i < rectangle.length; i++){
                for(int j = 0; j < rectangle[0].length; j++){
                    rotatedRectangle[j][i] = rectangle[i][j];
                }
            }
            
            for(int i = 0; i < rotatedRectangle.length / 2; i++){
                for(int j = 0; j < rotatedRectangle[0].length; j++){
                    int temp = rotatedRectangle[i][j];
                    rotatedRectangle[i][j] = rotatedRectangle[rotatedRectangle.length - i -1][j];
                    rotatedRectangle[rotatedRectangle.length - i -1][j] = temp;
                }
            }
            
            this.h = rotatedRectangle.length;
            this.w = rotatedRectangle[0].length;
            this.rectangle = rotatedRectangle;
        }
        
        @Override
        public boolean equals(Object obj){
            if (obj == null || getClass() != obj.getClass()) {
               return false;
            }
            SectionRectangle other = (SectionRectangle) obj;
            
            boolean isMatch = true;
            for(int i = 0; i < h; i++){
                if(!isMatch) break;
                for(int j = 0; j < w; j++){
                    if(this.rectangle[i][j] != other.rectangle[i][j]){
                        isMatch = false;
                        break;
                    }
                }
            }
            
            return isMatch;
        }
        
        private int[] findRectangleSize(List<int[]> section){
            int minX = Integer.MAX_VALUE;
            int maxX = 0;
            int minY = Integer.MAX_VALUE;
            int maxY = 0;
            
            for(int i = 0; i < section.size(); i++){
                int y = section.get(i)[0];
                int x = section.get(i)[1];
                
                minX = Math.min(minX, x);
                minY = Math.min(minY, y);
                maxX = Math.max(maxX, x);
                maxY = Math.max(maxY, y);
            }
            
            int w = maxX - minX + 1;
            int h = maxY - minY + 1;
            
            return new int[]{h, w, minY, minX};
        }
        
//         public void print(){
//             System.out.println(String.format("size : %d, w : %d, h : %d", size, w, h));
//             for(int i = 0; i < h; i++){
//                 for(int j = 0; j < w; j++){
//                     System.out.print(rectangle[i][j]);
//                     System.out.print(" ");
//                 }
//                 System.out.println();
//             }
            
//             System.out.println();
//         }
    }
    
    private void findSection(List<List<int[]>> sections, int[][] map, 
                             boolean[][] visited,int target, int y, int x){
        if(visited[y][x]) return; // 이미 방문한 경우
        visited[y][x] = true;
        
        if(map[y][x] != target) return; // 찾고자 하는 블록이 아닌 경우
        sections.get(sections.size()-1).add(new int[]{y,x});
        
        for(int[] dxy : dxys){
            int ny = y + dxy[0];
            int nx = x + dxy[1];
            if(0 > ny || ny >= map.length) continue; // 맵 범위에서 벗어난 경우
            if(0 > nx || nx >= map[0].length) continue; // 맵 범위에서 벗어난 경우
            findSection(sections, map, visited, target, ny, nx);
        }
        
    }
    
    public int solution(int[][] game_board, int[][] table) {
        int size = game_board.length;
        
        // find empty section in gameBoard
        List<List<int[]>> gameBoardEmptySections = new ArrayList<>();
        int emptySectionIndex = 0;
        boolean[][] gameBoardVisited = new boolean[size][size];
        for(int y = 0; y < size; y++){
            for(int x = 0; x < size; x++){
                if(!gameBoardVisited[y][x] && game_board[y][x] == 0){ // 아직 방문하지 않은 빈 공간인 경우
                    gameBoardEmptySections.add(new ArrayList<>());
                    findSection(gameBoardEmptySections, game_board, gameBoardVisited, 0, y, x);
                }
            }
        }
        
        // find piece section in table
        List<List<int[]>> tablePieceSections = new ArrayList<>();
        int pieceSectionIndex = 0;
        boolean[][] tableVisited = new boolean[size][size];
        for(int y = 0; y < size; y++){
            for(int x = 0; x < size; x++){
                if(!tableVisited[y][x] && table[y][x] == 1){ // 아직 방문하지 조각인 경우
                    tablePieceSections.add(new ArrayList<>());
                    findSection(tablePieceSections, table, tableVisited, 1, y, x);
                }
            }
        }
        
        // set sectionRectangle of gameBoard
        List<SectionRectangle> gameBoardSectionRectangles = new ArrayList<>();
        for(List<int[]> section : gameBoardEmptySections){
            gameBoardSectionRectangles.add(new SectionRectangle(section));
        }
        
        // set sectionRectangle of table
        List<SectionRectangle> tableSectionRectangles = new ArrayList<>();
        for(List<int[]> section : tablePieceSections){
            tableSectionRectangles.add(new SectionRectangle(section));
        }
        
        // compare sectionRectangles each other
        int fillBlockNum = 0;
        boolean[] usedTableSectionRectangle = new boolean[tableSectionRectangles.size()];
        
        for(SectionRectangle gameBoardSectionRectangle : gameBoardSectionRectangles){
            boolean isMatch = false;
            for(int i = 0; i < tableSectionRectangles.size(); i++){
                if(isMatch) break;
                SectionRectangle tableSectionRectangle = tableSectionRectangles.get(i);
                if(usedTableSectionRectangle[i]) continue; // 이미 사용한 조각
                if(gameBoardSectionRectangle.size != tableSectionRectangle.size) continue; // 크기가 다름
                
                for(int j = 0; j < 4; j++){ // 회전시키면서 블럭이 맞는지 확인
                    tableSectionRectangle.rotate();
                    // tableSectionRectangle.print();
                    
                    if(tableSectionRectangle.w != gameBoardSectionRectangle.w || 
                      tableSectionRectangle.h != gameBoardSectionRectangle.h) continue;
                    if(!gameBoardSectionRectangle.equals(tableSectionRectangle)) continue;
                    
                    // System.out.println("correct!!");
                    fillBlockNum += gameBoardSectionRectangle.size;
                    usedTableSectionRectangle[i] = true;
                    isMatch = true;
                    break;
                }
            }
        }
        
        return fillBlockNum;
    }
}