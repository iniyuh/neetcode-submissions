class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        int[] sQuants = new int[26];
        int[] tQuants = new int[26];

        int root = (int) 'a';

        s.chars().forEach(c -> sQuants[(int) c - root]++);
        t.chars().forEach(c -> tQuants[(int) c - root]++);

        return Arrays.equals(sQuants, tQuants);
    }
}
