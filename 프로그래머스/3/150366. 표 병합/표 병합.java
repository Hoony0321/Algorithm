import java.util.*;
class Solution {
    class Cell {
        String value;
        Cell parent;
        
        public Cell(){
            this.value = "";
            this.parent = this;
        }
        
        public String getValue(){
            return this.parent.value;
        }
        
        public void setValue(String value){
            this.parent.value = value;
        }
        
        public void setParent(Cell parent){
            this.parent = parent;
            this.value = "";
        }
        
        public void unsetParent(){
            this.parent = this;
            this.value = "";
        }
        
        @Override
        public String toString(){
            return this.getValue().equals("") ? "EMPTY" : this.getValue();
        }
    }
    
    class Table {
        Cell[][] cells;
        
        public Table(){
            cells = new Cell[51][51];
            
            for(int i = 1; i < 51; i++){
                for(int j = 1; j < 51; j++){
                    cells[i][j] = new Cell();
                }
            }
        }
        
        public void updateByPosition(int r, int c, String value){
            cells[r][c].setValue(value);
        }
        
        public void updateByValue(String value1, String value2){
            for(int r = 1; r < 51; r++){
                for(int c = 1; c < 51; c++){
                    if(cells[r][c].value.equals(value1)){
                        cells[r][c].value = value2;
                    }
                }
            }
        }
        
        public void merge(int r1, int c1, int r2, int c2){
            if(r1 == r2 && c1 == c2) return; // 같은 위치 셀인 경우 무시
            
            Cell cell1 = cells[r1][c1];
            Cell cell2 = cells[r2][c2];
            if(cell1.parent.equals(cell2.parent)) return;
            
            String mergeValue = cell1.getValue().equals("") ? 
                cell2.getValue() : 
                cell1.getValue();
            
            cell1.setValue(mergeValue);
            
            // update parent
            Cell cell2Parent = cell2.parent;
            for(int i = 1; i < 51; i++){
                for(int j = 1; j < 51; j++){
                    if(cells[i][j].parent.equals(cell2Parent)){
                        cells[i][j].setParent(cell1.parent);
                    }
                }
            }
        }
        
        public void unmerge(int r, int c){
            Cell parent = cells[r][c].parent;
            String parentValue = cells[r][c].getValue();
            
            // unset parent
            for(int i = 1; i < 51; i++){
                for(int j = 1; j < 51; j++){
                    if(cells[i][j].parent.equals(parent)){
                        cells[i][j].unsetParent();
                    }
                }
            }
            
            // cells[r][c]에 기존 부모 값 저장.
            cells[r][c].setValue(parentValue);
        }
        
        public String print(int r, int c){
            return cells[r][c].toString();
        }
    }
    
    public String[] solution(String[] commands) {
        Table table = new Table();
        List<String> printResult = new ArrayList<>();
        
        for(String command : commands){
            String[] splitedCommand = command.split(" ");
            String operator = splitedCommand[0];
            System.out.println();
            for(int i = 1; i < 5; i++){
                for(int j = 1; j < 5; j++){
                    System.out.print(table.cells[i][j]);
                    System.out.print(" ");
                }
                System.out.println();
            }

            if(operator.equals("UPDATE")){
                if(splitedCommand.length == 4){
                    int r = Integer.parseInt(splitedCommand[1]);
                    int c = Integer.parseInt(splitedCommand[2]);
                    String value = splitedCommand[3];
                    table.updateByPosition(r,c,value);
                }
                if(splitedCommand.length == 3){
                    String value1 = splitedCommand[1];
                    String value2 = splitedCommand[2];
                    table.updateByValue(value1,value2);
                }
            }
            
            if(operator.equals("MERGE")){
                int r1 = Integer.parseInt(splitedCommand[1]);
                int c1 = Integer.parseInt(splitedCommand[2]);
                int r2 = Integer.parseInt(splitedCommand[3]);
                int c2 = Integer.parseInt(splitedCommand[4]);
                table.merge(r1,c1,r2,c2);
            }
            
            if(operator.equals("UNMERGE")){
                int r = Integer.parseInt(splitedCommand[1]);
                int c = Integer.parseInt(splitedCommand[2]);
                table.unmerge(r,c);
            }
            
            if(operator.equals("PRINT")){
                int r = Integer.parseInt(splitedCommand[1]);
                int c = Integer.parseInt(splitedCommand[2]);
                printResult.add(table.print(r,c));
            }
            
        }
        
        String[] answer = new String[printResult.size()];
        for(int i = 0; i < printResult.size(); i++){
            answer[i] = printResult.get(i);
        }
        
        return answer;
    }
}