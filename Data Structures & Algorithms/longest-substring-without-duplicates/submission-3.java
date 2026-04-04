class Solution {
    public int lengthOfLongestSubstring(String s) {
        int longest = 0;
        int lefti = 0;
        int righti = 0;
        Map<Character, Number> seen = new HashMap<>();
        char[] str = s.toCharArray();
        for(int i = 0; i < str.length; ++i){
            char c = str[i];
            if(seen.containsKey(c)){
                System.out.println("goobye key: " + c);
                System.out.println(seen);
                int currenti = lefti;
                while(str[currenti] != c){
                    seen.remove(str[currenti]);
                    currenti += 1;
                }
                lefti = currenti+1;
            }
            else{
                seen.put(c, 1);
                righti += 1;
                longest = longest < seen.size() ? seen.size() : longest;
            }
        }
        return longest;
    }
}
