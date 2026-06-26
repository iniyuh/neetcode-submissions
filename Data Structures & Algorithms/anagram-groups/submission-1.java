class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> res = new HashMap<>();

        int root = (int) 'a';

        for (int i = 0; i < strs.length; i++) {
            int[] charCounts = new int[26];

            strs[i].chars().forEach(c -> charCounts[(int) c - root]++);

            String strRepresentation = Arrays.stream(charCounts).mapToObj(String::valueOf).collect(Collectors.joining("-"));
            
            res.putIfAbsent(strRepresentation, new ArrayList<>());
            res.get(strRepresentation).add(strs[i]);
        }

        return new ArrayList<>(res.values());
    }
}