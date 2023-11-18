import java.util.*;

class Solution {
    List<Character> operand = Arrays.asList('*', '+', '-');
    LinkedList<Long> originNumbers = new LinkedList<>();
    LinkedList<Character> originOperands = new LinkedList<>();
    List<List<Character>> priorities = new ArrayList<>();
    
    public long solution(String expression) {
        // 초기값 세팅
        long answer = 0;
        initNumbersAndOperands(expression);
        
        // 우선순위 배열 구하기
        int[] output = new int[3];
        boolean[] visited = new boolean[3];
        permutation(output,visited,0,3,3);
        
        // 우선순위대로 계산 진행
        for(List<Character> priority : priorities){
            LinkedList<Long> tmpNumbers = new LinkedList<>(originNumbers);
            LinkedList<Character> tmpOperands = new LinkedList<>(originOperands);
            long calculateResult = calculateByPriority(tmpNumbers, tmpOperands, priority);
            answer = Math.max(answer, Math.abs(calculateResult));
        }

        return answer;
    }
    
    public long calculateByPriority(LinkedList<Long> numbers, LinkedList<Character> operands, List<Character> priority){
        for(Character targetOperand : priority){
            int index = 0;
            while(index < operands.size()){
                if(operands.get(index) == targetOperand){
                    numbers.set(index, calculate(numbers.get(index), numbers.get(index+1), targetOperand));
                    numbers.remove(index+1);
                    operands.remove(index);
                }
                else{
                    index++;
                }
            }
        }
    
        return numbers.get(0);
    }
    
    public long calculate(long num1, long num2, char operand){
        if(operand == '*') return num1 * num2;
        if(operand == '+') return num1 + num2;
        if(operand == '-') return num1 - num2;
        return 0;
    }
    
    public void permutation(int[] output, boolean[] visited, int depth, int n, int r){
        if(r == 0){
            List<Character> priority = new ArrayList<>();
            for(int i = 0; i < n; i++){
                priority.add(operand.get(output[i]));
            }
            
            priorities.add(priority);
            return;
        }
        
        for(int i = 0; i < n; i++){
            if(!visited[i]){
                visited[i] = true;
                output[depth] = i;
                permutation(output,visited,depth+1, n, r-1);
                visited[i] = false;
            }
        }
    }
    
    public void initNumbersAndOperands(String expression){
        String[] splitExpression = expression.split("\\*|\\+|\\-");
        int index = -1;
        for(String splited : splitExpression){
            originNumbers.add(Long.parseLong(splited));
            index += splited.length() + 1;
            if(index > expression.length()-1) continue;
            originOperands.add(expression.charAt(index));
        }
    }
}