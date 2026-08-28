//장군 - 5/ 병정 - 3 / 일개미
class Solution {
    public int solution(int hp) {
        int answer = 0;
        
        //장군
        answer += hp/5;
        hp %= 5;
        
        answer += hp/3;
        hp %= 3;
        
        answer += hp;
        
        return answer;
    }
}