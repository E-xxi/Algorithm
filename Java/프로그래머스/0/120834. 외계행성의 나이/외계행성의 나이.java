class Solution {
    public String solution(int age) {
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        String answer = "";
        
        int num = 0;
        while (age > 0){
            num = age % 10;
            age = age / 10;
            
            answer += alphabet.charAt(num);
        }
        
        return new StringBuilder(answer).reverse().toString();
    }
}