class Solution {
    public boolean isValid(String s) {
        Stack<Character> opens = new Stack<>();
        if (s.length() % 2 != 0)
        return false;
        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if (c == '(' || c == '{' || c == '[')
            opens.push(c);
            else{
                if (opens.size() == 0)
                return false;
                char character = opens.pop();
                if ((character == '{' && c != '}') || (character == '[' && c != ']') || (character == '(' && c != ')'))
                return false;
            }
        }
        if (opens.size() != 0)
        return false;
        return true;
    }
}
