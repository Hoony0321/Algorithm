import java.util.*;

enum RobotStatus {
    READY, WORKING, DONE;
}

class Point {
    int y;
    int x;
    
    public Point(int y, int x){
        this.y = y;
        this.x = x;
    }
    
    @Override
    public boolean equals(Object o){
        Point point = (Point) o;
        return this.y == point.y && this.x == point.x;
    }
    
    @Override
    public int hashCode(){
        return Objects.hash(y, x);
    }
}

class Robot {
    Point curPoint = new Point(-1,-1);
    Deque<Point> route = new ArrayDeque<>();
    RobotStatus status = RobotStatus.READY;
    
    
    public Robot(Point[] route){
        for(Point point : route){
            this.route.addLast(point);
        }
    }
    
    public void move(){
        if(this.status == RobotStatus.DONE) return;
        
        Point nextPoint = route.getFirst();
        if(this.status == RobotStatus.READY){
            curPoint = new Point(nextPoint.y, nextPoint.x);
            this.status = RobotStatus.WORKING;
            route.removeFirst();
            return;
        }
        
        if(curPoint.y != nextPoint.y){
            if(curPoint.y < nextPoint.y){
                curPoint.y += 1;
            }
            else if(curPoint.y > nextPoint.y){
                curPoint.y -= 1;
            }
        }
        else if(curPoint.x != nextPoint.x){
            if(curPoint.x < nextPoint.x){
                curPoint.x += 1;
            }
            else if(curPoint.x > nextPoint.x){
                curPoint.x -= 1;
            }
        }
        
        if(curPoint.equals(nextPoint)){
            route.removeFirst();
            if(route.isEmpty()){
                this.status = RobotStatus.DONE;
            }
        }
    }
}

class Solution {
    public int solution(int[][] pointArray, int[][] routes) {
        int answer = 0;
        Point[] points = new Point[pointArray.length];
        Robot[] robots = new Robot[routes.length];
        
        for(int i = 0; i < pointArray.length; i++){
            points[i] = new Point(pointArray[i][0], pointArray[i][1]);
        }
        
        for(int i = 0; i < routes.length; i++){
            Point[] route = new Point[routes[i].length];
            for(int j = 0; j < route.length; j++){
                route[j] = points[routes[i][j]-1];
            }
            robots[i] = new Robot(route);
        }
        
        while(true){
            boolean finish = true;
            Map<Point, Integer> pointMap = new HashMap<>();
            for(Robot robot : robots){
                if(robot.status != RobotStatus.DONE){
                    robot.move();
                    pointMap.put(robot.curPoint, pointMap.getOrDefault(robot.curPoint,0) + 1);
                    finish = false;
                }
            }
            
            if(finish) break;
            
            // 충돌 체크
            for(Point key : pointMap.keySet()){
                if(pointMap.get(key) > 1){
                    answer += 1;
                }
            }
        }
        
        
        return answer;
    }
}