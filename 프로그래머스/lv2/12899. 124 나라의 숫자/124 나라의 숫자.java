import java.util.Stack;

class Solution {
    public String solution(int n) {
        String answer = "";
        Stack<Integer> answerStack = new Stack<>();
        int[] mapNumber = new int[3];
        mapNumber[0] = 4;
        mapNumber[1] = 1;
        mapNumber[2] = 2;
        
        while(n > 0){
            int rest = n % 3;
            n /= 3;
            if(rest == 0) n--;
            answerStack.push(mapNumber[rest]);
        }
        
        while(!answerStack.isEmpty()){
            answer += answerStack.pop();
        }
        
        return answer;
    }
}