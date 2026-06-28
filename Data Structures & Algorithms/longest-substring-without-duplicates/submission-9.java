class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() <= 1) return s.length();
        
        int l = 0, r = 1;
        int maxLength = 1;
        Set<Character> hs = new HashSet<>();
        hs.add(s.charAt(l));

        while (r < s.length()) {
            if (hs.contains(s.charAt(r))) {
                while (s.charAt(l) != s.charAt(r) && l < r - 1) {
                    hs.remove(s.charAt(l));
                    l++;
                }

                l++;
                r++;
            }
            else {
                hs.add(s.charAt(r));
                maxLength = Math.max(maxLength, r - l + 1);
                r++;
            }
        }

        return maxLength;
    }
}
