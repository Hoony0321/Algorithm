import java.util.*;

class Solution {
    class Table {
        Deque<Integer> leftSection  = new LinkedList<>();
        Deque<Deque<Integer>> centerSection = new LinkedList<>();
        Deque<Integer> rightSection = new LinkedList<>();
        
        public Table(int[][] rc){
            // set leftSection
            for(int i = 0; i < rc.length; i++){
                leftSection.add(rc[i][0]);
            }
            
            // set rightSection
            for(int i = 0; i < rc.length; i++){
                rightSection.add(rc[i][rc[0].length-1]);
            }
            
            // set centerSection
            for(int i = 0; i < rc.length; i++){
                centerSection.add(new LinkedList<>());
                for(int j = 1; j < rc[0].length-1; j++){
                    centerSection.peekLast().add(rc[i][j]);
                }
            }
        }
        
        public void rotate(){
            Deque<Integer> centerFirstSection = centerSection.peekFirst();
            Deque<Integer> centerLastSection = centerSection.peekLast();
            
            centerFirstSection.addFirst(leftSection.poll());
            rightSection.addFirst(centerFirstSection.pollLast());
            centerLastSection.addLast(rightSection.pollLast());
            leftSection.addLast(centerLastSection.poll());
        }
        
        public void shiftRow(){
            leftSection.addFirst(leftSection.pollLast());
            rightSection.addFirst(rightSection.pollLast());
            centerSection.addFirst(centerSection.pollLast());
        }
        
        public int[][] convertToArray(){
            int h = centerSection.size();
            int w = centerSection.isEmpty() ? 2 : centerSection.peek().size() + 2;
            int[][] array = new int[h][w];
            
            for(int i = 0; i < h; i++){
                array[i][0] = leftSection.poll();
                array[i][w-1] = rightSection.poll();
                
                Deque<Integer> centerSectionTop = centerSection.poll();
                int index = 1;
                while(!centerSectionTop.isEmpty()){
                    array[i][index++] = centerSectionTop.poll();
                }
            }
            
            return array;
        }
    }
    
    
    public int[][] solution(int[][] rc, String[] operations) {
        Table table = new Table(rc);
        
        for(String operation : operations){
            if(operation.equals("Rotate")){
                table.rotate();
            }
            
            if(operation.equals("ShiftRow")){
                table.shiftRow();
            }
        }
    
        return table.convertToArray();
    }
}