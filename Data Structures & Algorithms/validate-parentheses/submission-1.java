class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for(Character c : s.toCharArray()){
            if (c.equals('(') || c == '['|| c.equals('{')){
                stack.push(c);
            }
            else{
                if(stack.isEmpty()) return false;
                Character popped = stack.pop();
                if(popped.equals('(') && !c.equals(')')){
                    return false;
                }
                else if(popped.equals('{') && !c.equals('}')){
                    return false;
                }
                else if(popped.equals('[') && !c.equals(']')){
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
