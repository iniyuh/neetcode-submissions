class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> freq = new HashMap<>();

        for (char c : t.toCharArray()) {
            freq.merge(c, 1, Integer::sum);
        }

        int remainder = t.length();
        int l = 0, r = 0;

        while (remainder > 0 && r < s.length()) {
            char R = s.charAt(r);

            if (freq.containsKey(R)) {
                freq.merge(R, -1, Integer::sum);

                if (freq.get(R) >= 0) remainder--;
            }

            r++;
        }

        while (l < s.length() && (!freq.containsKey(s.charAt(l)) || freq.get(s.charAt(l)) < 0)) {
            if (freq.containsKey(s.charAt(l))) freq.merge(s.charAt(l), 1, Integer::sum);
            
            l++;
        }

        if (remainder > 0) return "";

        int minLength = r - l;
        String minString = s.substring(l, r);

        while (r < s.length()) {
            char R = s.charAt(r);
            if (freq.containsKey(R)) freq.merge(R, -1, Integer::sum);

            char L = s.charAt(l);
            while (!freq.containsKey(L) || freq.get(L) < 0) {
                if (freq.containsKey(L)) freq.merge(L, 1, Integer::sum);
                
                l++;
                L = s.charAt(l);
            }

            r++;

            if (r - l < minLength) {
                minLength = r - l;
                minString = s.substring(l, r);
            }
        }

        return minString;
    }
}
