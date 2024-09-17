class Solution {
    public String[] uncommonFromSentences(String s1, String s2) {
        Map<String, Integer> words = new HashMap<>();
        String[] str1 = s1.split(" ");
        String[] str2 = s2.split(" ");
        
        for (String str : str1) { 
            words.put(str, words.getOrDefault(str, 0) + 1);
        }
        for (String str : str2) {
            words.put(str, words.getOrDefault(str, 0) + 1);
        }

        List<String> uncommon = new ArrayList<>();
        for (Map.Entry<String, Integer> map : words.entrySet()) {
            if (map.getValue() == 1) {
                uncommon.add(map.getKey());
            }
        }

        return uncommon.toArray(new String[0]);
    }
}