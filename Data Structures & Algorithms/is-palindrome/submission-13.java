class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        
        int l = 0, r = s.length() - 1;
        char[] arr = s.toCharArray();

        while (l != r && l < r) {
            if (arr[l] != arr[r]) return false;
            l += 1;
            r -= 1;
        }

        return true;
    }
}
